import torch
import torch.nn as nn
import torch.optim as optim
import torchtext
import pandas as pd

data = pd.read_csv('depression.txt', header=None, sep='\t')  # my dataset
train_data, test_data = [], []
for i in range(4000):
    label = int(1) if data.values[i][1] == 'positive' else int(0)
    train_data.append((data.values[i][2], label))

for i in range(4000, data.shape[0]):
    label = int(1) if data.values[i][1] == 'positive' else int(0)
    test_data.append((data.values[i][2], label))
# print(train_data)
# 定义示例数据集
'''train_data = [("This movie is great", 1),
              ("The plot is boring", 0),
              ("The acting is terrible", 0),
              ("I love this movie", 1)]

# 进行预测
test_data = [("This movie is awesome!", 1),
             ("This movie is terrible", 0),
             ("The plot is interesting", 1),
             ("The acting is bad", 0)]'''

# 定义数据预处理的管道
TEXT = torchtext.data.Field(tokenize='spacy', tokenizer_language='en_core_web_sm')
LABEL = torchtext.data.LabelField(dtype=torch.float)

# 将数据转化为Dataset类型
train_examples = [torchtext.data.Example.fromlist([text, label], [('text', TEXT), ('label', LABEL)])
                  for text, label in train_data]
train_dataset = torchtext.data.Dataset(train_examples, [('text', TEXT), ('label', LABEL)])

# 构建词汇表
MAX_VOCAB_SIZE = 25_000
TEXT.build_vocab(train_dataset, max_size=MAX_VOCAB_SIZE)
LABEL.build_vocab(train_dataset)


# 定义模型
class RNN(nn.Module):
    def __init__(self, input_dim, embedding_dim, hidden_dim, output_dim):
        super().__init__()
        self.embedding = nn.Embedding(input_dim, embedding_dim)
        self.rnn = nn.LSTM(embedding_dim, hidden_dim)
        self.fc = nn.Linear(hidden_dim, output_dim)

    def forward(self, text):
        embedded = self.embedding(text)
        output, (hidden, cell) = self.rnn(embedded)
        assert torch.equal(output[-1, :, :], hidden.squeeze(0))
        return self.fc(hidden.squeeze(0))


# 初始化模型和超参数
INPUT_DIM = len(TEXT.vocab)
EMBEDDING_DIM = 1000
HIDDEN_DIM = 512
OUTPUT_DIM = 1

model = RNN(INPUT_DIM, EMBEDDING_DIM, HIDDEN_DIM, OUTPUT_DIM)

# 训练模型
optimizer = optim.Adam(model.parameters())
criterion = nn.BCEWithLogitsLoss()

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model = model.to(device)
criterion = criterion.to(device)


def binary_accuracy(preds, y):
    rounded_preds = torch.round(torch.sigmoid(preds))
    correct = (rounded_preds == y).float()
    acc = correct.sum() / len(correct)
    return acc


def train(model, iterator, optimizer, criterion):
    epoch_loss = 0
    epoch_acc = 0
    model.train()
    for batch in iterator:
        optimizer.zero_grad()
        text = batch.text
        predictions = model(text).squeeze(1)
        loss = criterion(predictions, batch.label)
        acc = binary_accuracy(predictions, batch.label)
        loss.backward()
        optimizer.step()
        epoch_loss += loss.item()
        epoch_acc += acc.item()
    return epoch_loss / len(iterator), epoch_acc / len(iterator)


N_EPOCHS = 100  # 大约不到50次收敛
train_iterator = torchtext.data.BucketIterator(
    train_dataset,
    batch_size=512,  # 占用大约2GB显存
    device=device,
    sort_within_batch=True,
    sort_key=lambda x: len(x.text)
)

for epoch in range(N_EPOCHS):
    train_loss, train_acc = train(model, train_iterator, optimizer, criterion)
    print(f'Epoch: {epoch + 1:02}')
    print(f'\tTrain Loss: {train_loss:.3f} | Train Acc: {train_acc * 100:.2f}%')


test_examples = [torchtext.data.Example.fromlist([text, label], [('text', TEXT), ('label', LABEL)])
                 for text, label in test_data]
test_dataset = torchtext.data.Dataset(test_examples, [('text', TEXT), ('label', LABEL)])
test_iterator = torchtext.data.Iterator(
    test_dataset,
    batch_size=(data.shape[0]-4000),
    device=device,
    sort_within_batch=True,
    sort_key=lambda x: len(x.text)
)
model.eval()
with torch.no_grad():
    for batch in test_iterator:
        text = batch.text
        predictions = model(text).squeeze(1)
        loss = criterion(predictions, batch.label)
        acc = binary_accuracy(predictions, batch.label)
        epoch_loss = loss.item()
        epoch_acc = acc.item()
        print(f'\tEval Loss: {epoch_loss:.3f} | Eval Acc: {epoch_acc * 100:.2f}%')