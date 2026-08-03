# Notebook validation report

**When:** 2026-08-03 00:42 UTC
**Scope:** Wave 1
**Result:** 3 passed, 12 failed, 15 total

| Notebook | Status | Seconds | Error |
|---|---|---:|---|
| `Chapter01/mnist_pytorch.ipynb` | fail | 29.84 | CellExecutionError: An error occurred while executing the following cell: ------------------ # The mean and standard deviation values are calculated as the mean of all pixel values |
| `Chapter01/pytorch2x_compile_demo.ipynb` | fail | 6.99 | CellExecutionError: An error occurred while executing the following cell: ------------------ tfm = transforms.Compose([     transforms.ToTensor(),     transforms.Normalize((0.1307, |
| `Chapter02/lenet.ipynb` | fail | 9.5 | CellExecutionError: An error occurred while executing the following cell: ------------------ # The mean and std are kept as 0.5 for normalizing pixel values as the pixel values are |
| `Chapter02/transfer_learning_alexnet.ipynb` | fail | 8.81 | CellExecutionError: An error occurred while executing the following cell: ------------------ ddir = 'hymenoptera_data'  # Data normalization and augmentation transformations for tr |
| `Chapter02/vgg13_pretrained_run_inference.ipynb` | fail | 7.64 | CellExecutionError: An error occurred while executing the following cell: ------------------ ddir = 'hymenoptera_data'  # Data normalization and augmentation transformations for tr |
| `Chapter02/ResNetBlock.ipynb` | pass | 4.85 |  |
| `Chapter02/DenseNetBlock.ipynb` | pass | 2.32 |  |
| `Chapter02/GoogLeNet.ipynb` | pass | 4.41 |  |
| `Chapter03/rnn.ipynb` | fail | 5.57 | CellExecutionError: An error occurred while executing the following cell: ------------------ # read sentiments and reviews data from the text files review_list = [] label_list = [] |
| `Chapter03/lstm.ipynb` | fail | 5.97 | CellExecutionError: An error occurred while executing the following cell: ------------------ import random from torchtext.legacy import datasets from torchtext.legacy import data - |
| `Chapter15/fastai.ipynb` | fail | 37.98 | CellExecutionError: An error occurred while executing the following cell: ------------------ path = untar_data(URLs.MNIST) print(path) ------------------   [31m------------------- |
| `Chapter15/pytorch_lightning.ipynb` | fail | 12.55 | CellExecutionError: An error occurred while executing the following cell: ------------------ model = ConvNet()  trainer = pl.Trainer(max_epochs=10)     trainer.fit(model)    ------ |
| `Chapter15/pytorch_profiler.ipynb` | fail | 5.96 | CellExecutionError: An error occurred while executing the following cell: ------------------ # The mean and standard deviation values are calculated as the mean of all pixel values |
| `Chapter17/captum_interpretability.ipynb` | fail | 7.15 | CellExecutionError: An error occurred while executing the following cell: ------------------ # The mean and standard deviation values are calculated as the mean of all pixel values |
| `Chapter17/pytorch_interpretability.ipynb` | fail | 7.41 | CellExecutionError: An error occurred while executing the following cell: ------------------ # The mean and standard deviation values are calculated as the mean of all pixel values |

## Failures (detail)

### `Chapter01/mnist_pytorch.ipynb`
```
Traceback (most recent call last):
  File "/Users/ashish/code/MasteringPyTorchV3/scripts/validate_notebooks.py", line 85, in run_one
    client.execute()
  File "/Users/ashish/code/MasteringPyTorchV3/.venv/lib/python3.11/site-packages/jupyter_core/utils/__init__.py", line 165, in wrapped
    return loop.run_until_complete(inner)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/asyncio/base_events.py", line 654, in run_until_complete
    return future.result()
           ^^^^^^^^^^^^^^^
  File "/Users/ashish/code/MasteringPyTorchV3/.venv/lib/python3.11/site-packages/nbclient/client.py", line 709, in async_execute
    await self.async_execute_cell(
  File "/Users/ashish/code/MasteringPyTorchV3/.venv/lib/python3.11/site-packages/nbclient/client.py", line 1062, in async_execute_cell
    await self._check_raise_for_error(cell, cell_index, exec_reply)
  File "/Users/ashish/code/MasteringPyTorchV3/.venv/lib/python3.11/site-packages/nbclient/client.py", line 918, in _check_raise_for_error
    raise CellExecutionError.from_cell_and_msg(cell, exec_reply_content)
nbclient.exceptions.CellExecutionError: An error occurred while executing the following cell:
------------------
# The mean and standard deviation values are calculated as the mean of all pixel values of all images in the training dataset
train_dataloader = torch.utils.data.DataLoader(
    datasets.MNIST('../data', train=True, download=True,
                   transform=transforms.Compose([
                       transforms.ToTensor(),
                       transforms.Normalize((0.1302,), (0.3069,))])), # train_X.mean()/256. and train_X.std()/256.
    batch_size=32, shuffle=True)

test_dataloader = torch.utils.data.DataLoader(
    datasets.MNIST('../data', train=False, 
                   transform=transforms.Compose([
                       transforms.ToTensor(),
                       transforms.Normalize((0.1302,), (0.3069,)) 
                   ])),
    batch_size=500, shuffle=False)
------------------


[31m---------------------------------------------------------------------------[39m
[31mRuntimeError[39m                              Traceback (most recent call last)
[36mCell[39m[36m [39m[32mIn[6][39m[32m, line 3[39m
[32m      1[39m [38;5;66;03m# The mean and standard deviation values are calculated as the mean of all pixel values of all images in the training dataset[39;00m
[32m      2[39m train_dataloader = torch.utils.data.DataLoader(
[32m----> [39m[32m3[39m     datasets.MNIST('../data', train=True, download=True,
[32m      4[39m                    transform=transforms.Compose([
[32m      5[39m                        transforms.ToTensor(),
[32m      6[39m                        transforms.Normalize((0.1302,), (0.3069,))])), # train_X.mean()/256. and train_X.std()/256.

[36mFile [39m[32m~/code/MasteringPyTorchV3/.venv/lib/python3.11/site-packages/torchvision/datasets/mnist.py:100[39m, in [36mMNIST.__init__[39m[34m(self, root, train, transform, target_transform, download)[39m
[32m     97[39m     [38;5;28;01mreturn[39;00m
[32m     99[39m [38;5;28;01mif[39;00m download:
[32m--> [39m[32m100[39m     [30;43mself[39;49m[30;43m.[39;49m[30;43mdownload[39;49m[30;43m([39;49m[30;43m)[39;49m
[32m    102[39m [38;5;28;01mif[39;00m [38;5;129;01mnot[39;00m [38;5;28mself[39m._check_exists():
[32m    103[39m     [38;5;28;01mraise[39;00m [38;5;167;01mRuntimeError[39;00m([33m"[39m[33mDataset not found. You can use download=True to download it[39m[33m"[39m)

[36mFile [39m[32m~/code/MasteringPyTorchV3/.venv/lib/python3.11/site-packages/torchvision/datasets/mnist.py:197[39m, in [36mMNIST.download[39m[34m(self)[39m
[32m    195[39m [38;5;28;01mfor[39;00m mirror, err [38;5;129;01min[39;00m [38;5;28mzip[39m([38;5;28mself[39m.mirrors, errors):
[32m    196[39m     s += [33mf[39m[33m"[39m[33mTried [39m[38;5;132;01m{[39;00mmirror[38;5;132;01m}[39;00m[33m, got:[39m[38;5;130;01m\n[39;00m[38;5;132;01m{[39;00m[38;5;28mstr[39m(err)[38;5;132;01m}[39;00m[38;5;130;01m\n[39;00m[33m"[39m
[32m--> [39m[32m197[39m [38;5;28;01mraise[39;00m [38;5;167;01mRuntimeError[39;00m(s)

[31mRuntimeError[39m: Error downloading train-images-idx3-ubyte.gz:
Tried https://ossci-datasets.s3.amazonaws.com/mnist/, got:
<urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1006)>
Tried http://yann.lecun.com/exdb/mnist/, got:
HTTP Error 404: Not Found



```

### `Chapter01/pytorch2x_compile_demo.ipynb`
```
Traceback (most recent call last):
  File "/Users/ashish/code/MasteringPyTorchV3/scripts/validate_notebooks.py", line 85, in run_one
    client.execute()
  File "/Users/ashish/code/MasteringPyTorchV3/.venv/lib/python3.11/site-packages/jupyter_core/utils/__init__.py", line 165, in wrapped
    return loop.run_until_complete(inner)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/asyncio/base_events.py", line 654, in run_until_complete
    return future.result()
           ^^^^^^^^^^^^^^^
  File "/Users/ashish/code/MasteringPyTorchV3/.venv/lib/python3.11/site-packages/nbclient/client.py", line 709, in async_execute
    await self.async_execute_cell(
  File "/Users/ashish/code/MasteringPyTorchV3/.venv/lib/python3.11/site-packages/nbclient/client.py", line 1062, in async_execute_cell
    await self._check_raise_for_error(cell, cell_index, exec_reply)
  File "/Users/ashish/code/MasteringPyTorchV3/.venv/lib/python3.11/site-packages/nbclient/client.py", line 918, in _check_raise_for_error
    raise CellExecutionError.from_cell_and_msg(cell, exec_reply_content)
nbclient.exceptions.CellExecutionError: An error occurred while executing the following cell:
------------------
tfm = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize((0.1307,), (0.3081,)),
])
ds = datasets.MNIST(root="./data", train=False, download=True, transform=tfm)
x = torch.stack([ds[i][0] for i in range(64)]).to(device)

@torch.inference_mode()
def bench(fn, warmup=5, iters=50):
    for _ in range(warmup):
        fn(x)
    if device.type == "cuda":
        torch.cuda.synchronize()
    t0 = time.perf_counter()
    for _ in range(iters):
        fn(x)
    if device.type == "cuda":
        torch.cuda.synchronize()
    return (time.perf_counter() - t0) / iters * 1000

eager_ms = bench(model)
compiled_ms = bench(compiled)
print(f"eager:     {eager_ms:.3f} ms / batch")
print(f"compiled:  {compiled_ms:.3f} ms / batch")
print(f"speedup:   {eager_ms / compiled_ms:.2f}x")

------------------


[31m---------------------------------------------------------------------------[39m
[31mRuntimeError[39m                              Traceback (most recent call last)
[36mCell[39m[36m [39m[32mIn[3][39m[32m, line 5[39m
[32m      1[39m tfm = transforms.Compose([
[32m      2[39m     transforms.ToTensor(),
[32m      3[39m     transforms.Normalize(([32m0.1307[39m,), ([32m0.3081[39m,)),
[32m      4[39m ])
[32m----> [39m[32m5[39m ds = datasets.MNIST(root=[33m"./data"[39m, train=[38;5;28;01mFalse[39;00m, download=[38;5;28;01mTrue[39;00m, transform=tfm)
[32m      6[39m x = torch.stack([ds[i][[32m0[39m] [38;5;28;01mfor[39;00m i [38;5;28;01min[39;00m range([32m64[39m)]).to(device)
[32m      7[39m 
[32m      8[39m @torch.inference_mode()

[36mFile [39m[32m~/code/MasteringPyTorchV3/.venv/lib/python3.11/site-packages/torchvision/datasets/mnist.py:100[39m, in [36mMNIST.__init__[39m[34m(self, root, train, transform, target_transform, download)[39m
[32m     97[39m     [38;5;28;01mreturn[39;00m
[32m     99[39m [38;5;28;01mif[39;00m download:
[32m--> [39m[32m100[39m     [30;43mself[39;49m[30;43m.[39;49m[30;43mdownload[39;49m[30;43m([39;49m[30;43m)[39;49m
[32m    102[39m [38;5;28;01mif[39;00m [38;5;129;01mnot[39;00m [38;5;28mself[39m._check_exists():
[32m    103[39m     [38;5;28;01mraise[39;00m [38;5;167;01mRuntimeError[39;00m([33m"[39m[33mDataset not found. You can use download=True to download it[39m[33m"[39m)

[36mFile [39m[32m~/code/MasteringPyTorchV3/.venv/lib/python3.11/site-packages/torchvision/datasets/mnist.py:197[39m, in [36mMNIST.download[39m[34m(self)[39m
[32m    195[39m [38;5;28;01mfor[39;00m mirror, err [38;5;129;01min[39;00m [38;5;28mzip[39m([38;5;28mself[39m.mirrors, errors):
[32m    196[39m     s += [33mf[39m[33m"[39m[33mTried [39m[38;5;132;01m{[39;00mmirror[38;5;132;01m}[39;00m[33m, got:[39m[38;5;130;01m\n[39;00m[38;5;132;01m{[39;00m[38;5;28mstr[39m(err)[38;5;132;01m}[39;00m[38;5;130;01m\n[39;00m[33m"[39m
[32m--> [39m[32m197[39m [38;5;28;01mraise[39;00m [38;5;167;01mRuntimeError[39;00m(s)

[31mRuntimeError[39m: Error downloading train-images-idx3-ubyte.gz:
Tried https://ossci-datasets.s3.amazonaws.com/mnist/, got:
<urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1006)>
Tried http://yann.lecun.com/exdb/mnist/, got:
HTTP Error 404: Not Found



```

### `Chapter02/lenet.ipynb`
```
Traceback (most recent call last):
  File "/Users/ashish/code/MasteringPyTorchV3/scripts/validate_notebooks.py", line 85, in run_one
    client.execute()
  File "/Users/ashish/code/MasteringPyTorchV3/.venv/lib/python3.11/site-packages/jupyter_core/utils/__init__.py", line 165, in wrapped
    return loop.run_until_complete(inner)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/asyncio/base_events.py", line 654, in run_until_complete
    return future.result()
           ^^^^^^^^^^^^^^^
  File "/Users/ashish/code/MasteringPyTorchV3/.venv/lib/python3.11/site-packages/nbclient/client.py", line 709, in async_execute
    await self.async_execute_cell(
  File "/Users/ashish/code/MasteringPyTorchV3/.venv/lib/python3.11/site-packages/nbclient/client.py", line 1062, in async_execute_cell
    await self._check_raise_for_error(cell, cell_index, exec_reply)
  File "/Users/ashish/code/MasteringPyTorchV3/.venv/lib/python3.11/site-packages/nbclient/client.py", line 918, in _check_raise_for_error
    raise CellExecutionError.from_cell_and_msg(cell, exec_reply_content)
nbclient.exceptions.CellExecutionError: An error occurred while executing the following cell:
------------------
# The mean and std are kept as 0.5 for normalizing pixel values as the pixel values are originally in the range 0 to 1
train_transform = transforms.Compose([transforms.RandomHorizontalFlip(),
                                      transforms.RandomCrop(32, 4),
                                      transforms.ToTensor(),
                                      transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))])

trainset = torchvision.datasets.CIFAR10(root='./data', train=True, download=True, transform=train_transform)
trainloader = torch.utils.data.DataLoader(trainset, batch_size=8, shuffle=True)


test_transform = transforms.Compose([transforms.ToTensor(), transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))])

testset = torchvision.datasets.CIFAR10(root='./data', train=False, download=True, transform=test_transform)
testloader = torch.utils.data.DataLoader(testset, batch_size=10000, shuffle=False)


# ordering is important
classes = ('plane', 'car', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck')
------------------


[31m---------------------------------------------------------------------------[39m
[31mSSLCertVerificationError[39m                  Traceback (most recent call last)
[36mFile [39m[32m/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/urllib/request.py:1348[39m, in [36mAbstractHTTPHandler.do_open[39m[34m(self, http_class, req, **http_conn_args)[39m
[32m   1347[39m [38;5;28;01mtry[39;00m:
[32m-> [39m[32m1348[39m     [30;43mh[39;49m[30;43m.[39;49m[30;43mrequest[39;49m[30;43m([39;49m[30;43mreq[39;49m[30;43m.[39;49m[30;43mget_method[39;49m[30;43m([39;49m[30;43m)[39;49m[30;43m,[39;49m[30;43m [39;49m[30;43mreq[39;49m[30;43m.[39;49m[30;43mselector[39;49m[30;43m,[39;49m[30;43m [39;49m[30;43mreq[39;49m[30;43m.[39;49m[30;43mdata[39;49m[30;43m,[39;49m[30;43m [39;49m[30;43mheaders[39;49m[30;43m,[39;49m
[32m   1349[39m [30;43m              [39;49m[30;43mencode_chunked[39;49m[30;43m=[39;49m[30;43mreq[39;49m[30;43m.[39;49m[30;43mhas_header[39;49m[30;43m([39;49m[30;43m'[39;49m[30;43mTransfer-encoding[39;49m[30;43m'[39;49m[30;43m)[39;49m[30;43m)[39;49m
[32m   1350[39m [38;5;28;01mexcept[39;00m [38;5;167;01mOSError[39;00m [38;5;28;01mas[39;00m err: [38;5;66;03m# timeout error[39;00m

[36mFile [39m[32m/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/http/client.py:1303[39m, in [36mHTTPConnection.request[39m[34m(self, method, url, body, headers, encode_chunked)[39m
[32m   1302[39m [38;5;250m[39m[33;03m"""Send a complete request to the server."""[39;00m
[32m-> [39m[32m1303[39m [30;43mself[39;49m[30;43m.[39;49m[30;43m_send_request[39;49m[30;43m([39;49m[30;43mmethod[39;49m[30;43m,[39;49m[30;43m [39;49m[30;43murl[39;49m[30;43m,[39;49m[30;43m [39;49m[30;43mbody[39;49m[30;43m,[39;49m[30;43m [39;49m[30;43mheaders[39;49m[30;43m,[39;49m[30;43m [39;49m[30;43mencode_chunked[39;49m[30;43m)[39;49m

[36mFile [39m[32m/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/http/client.py:1349[39m, in [36mHTTPConnection._send_request[39m[34m(self, method, url, body, headers, encode_chunked)[39m
[32m   1348[39m     body = _encode(body, [33m'[39m[33mbody[39m[33m'[39m)
[32m-> [39m[32m1349[39m [30;43mself[39;49m[30;43m.[39;49m[30;43mendheaders[39;49m[30;43m([39;49m[30;43mbody[39;49m[30;43m,[39;49m[30;43m [39;49m[30;43mencode_chunked[39;49m[30;43m=[39;49m[30;43mencode_chunked[39;49m[30;43m)[39;49m

[36mFile [39m[32m/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/http/client.py:1298[39m, in [36mHTTPConnection.endheaders[39m[34m(self, message_body, encode_chunked)[39m
[32m   1297[39m     [38;5;28;01mraise[39;00m CannotSendHeader()
[32m-> [39m[32m1298[39m [30;43mself[39;49m[30;43m.[39;49m[30;43m_send_output[39;49m[30;43m([39;49m[30;43mmessage_body[39;49m[30;43m,[39;49m[30;43m [39;49m[30;43mencode_chunked[39;49m[30;43m=[39;49m[30;43mencode_chunked[39;49m[30;43m)[39;49m

[36mFile [39m[32m/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/http/client.py:1058[39m, in [36mHTTPConnection._send_output[39m[34m(self, message_body, encode_chunked)[39m
[32m   1057[39m [38;5;28;01mdel[39;00m [38;5;28mself[39m._buffer[:]
[32m-> [39m[32m1058[39m [30;43mself[39;49m[30;43m.[39;49m[30;43msend[39;49m[30;43m([39;49m[30;43mmsg[39;49m[30;43m)[39;49m
[32m   1060[39m [38;5;28;01mif[39;00m message_body [38;5;129;01mis[39;00m [38;5;129;01mnot[39;00m [38;5;28;01mNone[39;00m:
[32m   1061[39m 
[32m   1062[39m     [38;5;66;03m# create a consistent interface to message_body[39;00m

[36mFile [39m[32m/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/http/client.py:996[39m, in [36mHTTPConnection.send[39m[34m(self, data)[39m
[32m    995[39m [38;5;28;01mif[39;00m [38;5;28mself[39m.auto_open:
[32m--> [39m[32m996[39m     [30;43mself[39;49m[30;43m.[39;49m[30;43mconnect[39;49m[30;43m([39;49m[30;43m)[39;49m
[32m    997[39m [38;5;28;01melse[39;00m:

[36mFile [39m[32m/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/http/client.py:1475[39m, in [36mHTTPSConnection.connect[39m[34m(self)[39m
[32m   1473[39m     server_hostname = [38;5;28mself[39m.host
[32m-> [39m[32m1475[39m [38;5;28mself[39m.sock = [30;43mself[39;49m[30;43m.[39;49m[30;43m_context[39;49m[30;43m.[39;49m[30;43mwrap_socket[39;49m[30;43m([39;49m[30;43mself[39;49m[30;43m.[39;49m[30;43msock[39;49m[30;43m,[39;49m
[32m   1476[39m [30;43m                                      [39;49m[30;43mserver_hostname[39;49m[30;43m=[39;49m[30;43mserver_hostname[39;49m[30;43m)[39;49m

[36mFile [39m[32m/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/ssl.py:517[39m, in [36mSSLContext.wrap_socket[39m[34m(self, sock, server_side, do_handshake_on_connect, suppress_ragged_eofs, server_hostname, session)[39m
[32m    511[39m [38;5;28;01mdef[39;00m[38;5;250m [39m[34mwrap_socket[39m([38;5;28mself[39m, sock, server_side=[38;5;28;01mFalse[39;00m,
[32m    512[39m                 do_handshake_on_connect=[38;5;28;01mTrue[39;00m,
[32m    513[39m                 suppress_ragged_eofs=[38;5;28;01mTrue[39;00m,
[32m    514[39m                 server_hostname=[38;5;28;01mNone[39;00m, session=[38;5;28;01mNone[39;00m):
[32m    515[39m     [38;5;66;03m# SSLSocket class handles server_hostname encoding before it calls[39;00m
[32m    516[39m     [38;5;66;03m# ctx._wrap_socket()[39;00m
[32m--> [39m[32m517[39m     [38;5;28;01mreturn[39;00m [30;43mself[39;49m[30;43m.[39;49m[30;43msslsocket_class[39;49m[30;43m.[39;49m[30;43m_create[39;49m[30;43m([39;49m
[32m    518[39m [30;43m        [39;49m[30;43msock[39;49m[30;43m=[39;49m[30;43msock[39;49m[30;43m,[39;49m
[32m    519[39m [30;43m        [39;49m[30;43mserver_side[39;49m[30;43m=[39;49m[30;43mserver_side[39;49m[30;43m,[39;49m
[32m    520[39m [30;43m        [39;49m[30;43mdo_handshake_on_connect[39;49m[30;43m=[39;49m[30;43mdo_handshake_on_connect[39;49m[30;43m,[39;49m
[32m    521[39m [30;43m        [39;49m[30;43msuppress_ragged_eofs[39;49m[30;43m=[39;49m[30;43msuppress_ragged_eofs[39;49m[30;43m,[39;49m
[32m    522[39m [30;43m        [39;49m[30;43mserver_hostname[39;49m[30;43m=[39;49m[30;43mserver_hostname[39;49m[30;43m,[39;49m
[32m    523[39m [30;43m        [39;49m[30;43mcontext[39;49m[30;43m=[39;49m[30;43mself[39;49m[30;43m,[39;49m
[32m    524[39m [30;43m        [39;49m[30;43msession[39;49m[30;43m=[39;49m[30;43msession[39;49m
[32m    525[39m [30;43m    [39;49m[30;43m)[39;49m

[36mFile [39m[32m/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/ssl.py:1104[39m, in [36mSSLSocket._create[39m[34m(cls, sock, server_side, do_handshake_on_connect, suppress_ragged_eofs, server_hostname, context, session)[39m
[32m   1103[39m                 [38;5;28;01mraise[39;00m [38;5;167;01mValueError[39;00m([33m"[39m[33mdo_handshake_on_connect should not be specified for non-blocking sockets[39m[33m"[39m)
[32m-> [39m[32m1104[39m             [30;43mself[39;49m[30;43m.[39;49m[30;43mdo_handshake[39;49m[30;43m([39;49m[30;43m)[39;49m
[32m   1105[39m [38;5;28;01mexcept[39;00m:

[36mFile [39m[32m/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/ssl.py:1382[39m, in [36mSSLSocket.do_handshake[39m[34m(self, block)[39m
[32m   1381[39m         [38;5;28mself[39m.settimeout([38;5;28;01mNone[39;00m)
[32m-> [39m[32m1382[39m     [30;43mself[39;49m[30;43m.[39;49m[30;43m_sslobj[39;49m[30;43m.[39;49m[30;43mdo_handshake[39;49m[30;43m([39;49m[30;43m)[39;49m
[32m   1383[39m [38;5;28;01mfinally[39;00m:

[31mSSLCertVerificationError[39m: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1006)

During handling of the above exception, another exception occurred:

[31mURLError[39m                                  Traceback (most recent call last)
[36mCell[39m[36m [39m[32mIn[6][39m[32m, line 7[39m
[32m      3[39m                                       transforms.RandomCrop([32m32[39m, [32m4[39m),
[32m      4[39m                                       transforms.ToTensor(),
[32m      5[39m                                       transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))])
[32m      6[39m 
[32m----> [39m[32m7[39m trainset = torchvision.datasets.CIFAR10(root=[33m'./data'[39m, train=[38;5;28;01mTrue[39;00m, download=[38;5;28;01mTrue[39;00m, transform=train_transform)
[32m      8[39m trainloader = torch.utils.data.DataLoader(trainset, batch_size=[32m8[39m, shuffle=[38;5;28;01mTrue[39;00m)
[32m      9[39m 
[32m     10[39m 

[36mFile [39m[32m~/code/MasteringPyTorchV3/.venv/lib/python3.11/site-packages/torchvision/datasets/cifar.py:66[39m, in [36mCIFAR10.__init__[39m[34m(self, root, train, transform, target_transform, download)[39m
[32m     63[39m [38;5;28mself[39m.train = train  [38;5;66;03m# training set or test set[39;00m
[32m     65[39m [38;5;28;01mif[39;00m download:
[32m---> [39m[32m66[39m     [30;43mself[39;49m[30;43m.[39;49m[30;43mdownload[39;49m[30;43m([39;49m[30;43m)[39;49m
[32m     68[39m [38;5;28;01mif[39;00m [38;5;129;01mnot[39;00m [38;5;28mself[39m._check_integrity():
[32m     69[39m     [38;5;28;01mraise[39;00m [38;5;167;01mRuntimeError[39;00m([33m"[39m[33mDataset not found or corrupted. You can use download=True to download it[39m[33m"[39m)

[36mFile [39m[32m~/code/MasteringPyTorchV3/.venv/lib/python3.11/site-packages/torchvision/datasets/cifar.py:139[39m, in [36mCIFAR10.download[39m[34m(self)[39m
[32m    137[39m [38;5;28;01mif[39;00m [38;5;28mself[39m._check_integrity():
[32m    138[39m     [38;5;28;01mreturn[39;00m
[32m--> [39m[32m139[39m [30;43mdownload_and_extract_archive[39;49m[30;43m([39;49m[30;43mself[39;49m[30;43m.[39;49m[30;43murl[39;49m[30;43m,[39;49m[30;43m [39;49m[30;43mself[39;49m[30;43m.[39;49m[30;43mroot[39;49m[30;43m,[39;49m[30;43m [39;49m[30;43mfilename[39;49m[30;43m=[39;49m[30;43mself[39;49m[30;43m.[39;49m[30;43mfilename[39;49m[30;43m,[39;49m[30;43m [39;49m[30;43mmd5[39;49m[30;43m=[39;49m[30;43mself[39;49m[30;43m.[39;49m[30;43mtgz_md5[39;49m[30;43m)[39;49m

[36mFile [39m[32m~/code/MasteringPyTorchV3/.venv/lib/python3.11/site-packages/torchvision/datasets/utils.py:388[39m, in [36mdownload_and_extract_archive[39m[34m(url, download_root, extract_root, filename, md5, remove_finished)[39m
[32m    385[39m [38;5;28;01mif[39;00m [38;5;129;01mnot[39;00m filename:
[32m    386[39m     filename = os.path.basename(url)
[32m--> [39m[32m388[39m [30;43mdownload_url[39;49m[30;43m([39;49m[30;43murl[39;49m[30;43m,[39;49m[30;43m [39;49m[30;43mdownload_root[39;49m[30;43m,[39;49m[30;43m [39;49m[30;43mfilename[39;49m[30;43m,[39;49m[30;43m [39;49m[30;43mmd5[39;49m[30;43m)[39;49m
[32m    390[39m archive = os.path.join(download_root, filename)
[32m    391[39m extract_archive(archive, extract_root, remove_finished)

[36mFile [39m[32m~/code/MasteringPyTorchV3/.venv/lib/python3.11/site-packages/torchvision/datasets/utils.py:118[39m, in [36mdownload_url[39m[34m(url, root, filename, md5, max_redirect_hops)[39m
[32m    115[39m     _download_file_from_remote_location(fpath, url)
[32m    116[39m [38;5;28;01melse[39;00m:
[32m    117[39m     [38;5;66;03m# expand redirect chain if needed[39;00m
[32m--> [39m[32m118[39m     url = [30;43m_get_redirect_url[39;49m[30;43m([39;49m[30;43murl[39;49m[30;43m,[39;49m[30;43m [39;49m[30;43mmax_hops[39;49m[30;43m=[39;49m[30;43mmax_redirect_hops[39;49m[30;43m)[39;49m
[32m    120[39m     [38;5;66;03m# check if file is located on Google Drive[39;00m
[32m    121[39m     file_id = _get_google_drive_file_id(url)

[36mFile [39m[32m~/code/MasteringPyTorchV3/.venv/lib/python3.11/site-packages/torchvision/datasets/utils.py:63[39m, in [36m_get_redirect_url[39m[34m(url, max_hops)[39m
[32m     60[39m headers = {[33m"[39m[33mMethod[39m[33m"[39m: [33m"[39m[33mHEAD[39m[33m"[39m, [33m"[39m[33mUser-Agent[39m[33m"[39m: USER_AGENT}
[32m     62[39m [38;5;28;01mfor[39;00m _ [38;5;129;01min[39;00m [38;5;28mrange[39m(max_hops + [32m1[39m):
[32m---> [39m[32m63[39m     [38;5;28;01mwith[39;00m [30;43murllib[39;49m[30;43m.[39;49m[30;43mrequest[39;49m[30;43m.[39;49m[30;43murlopen[39;49m[30;43m([39;49m[30;43murllib[39;49m[30;43m.[39;49m[30;43mrequest[39;49m[30;43m.[39;49m[30;43mRequest[39;49m[30;43m([39;49m[30;43murl[39;49m[30;43m,[39;49m[30;43m [39;49m[30;43mheaders[39;49m[30;43m=[39;49m[30;43mheaders[39;49m[30;43m)[39;49m[30;43m)[39;49m [38;5;28;01mas[39;00m response:
[32m     64[39m         [38;5;28;01mif[39;00m response.url == url [38;5;129;01mor[39;00m response.url [38;5;129;01mis[39;00m [38;5;28;01mNone[39;00m:
[32m     65[39m             [38;5;28;01mreturn[39;00m url

[36mFile [39m[32m/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/urllib/request.py:216[39m, in [36murlopen[39m[34m(url, data, timeout, cafile, capath, cadefault, context)[39m
[32m    214[39m [38;5;28;01melse[39;00m:
[32m    215[39m     opener = _opener
[32m--> [39m[32m216[39m [38;5;28;01mreturn[39;00m [30;43mopener[39;49m[30;43m.[39;49m[30;43mopen[39;49m[30;43m([39;49m[30;43murl[39;49m[30;43m,[39;49m[30;43m [39;49m[30;43mdata[39;49m[30;43m,[39;49m[30;43m [39;49m[30;43mtimeout[39;49m[30;43m)[39;49m

[36mFile [39m[32m/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/urllib/request.py:519[39m, in [36mOpenerDirector.open[39m[34m(self, fullurl, data, timeout)[39m
[32m    516[39m     req = meth(req)
[32m    518[39m sys.audit([33m'[39m[33murllib.Request[39m[33m'[39m, req.full_url, req.data, req.headers, req.get_method())
[32m--> [39m[32m519[39m response = [30;43mself[39;49m[30;43m.[39;49m[30;43m_open[39;49m[30;43m([39;49m[30;43mreq[39;49m[30;43m,[39;49m[30;43m [39;49m[30;43mdata[39;49m[30;43m)[39;49m
[32m    521[39m [38;5;66;03m# post-process response[39;00m
[32m    522[39m meth_name = protocol+[33m"[39m[33m_response[39m[33m"[39m

[36mFile [39m[32m/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/urllib/request.py:536[39m, in [36mOpenerDirector._open[39m[34m(self, req, data)[39m
[32m    533[39m     [38;5;28;01mreturn[39;00m result
[32m    535[39m protocol = req.type
[32m--> [39m[32m536[39m result = [30;43mself[39;49m[30;43m.[39;49m[30;43m_call_chain[39;49m[30;43m([39;49m[30;43mself[39;49m[30;43m.[39;49m[30;43mhandle_open[39;49m[30;43m,[39;49m[30;43m [39;49m[30;43mprotocol[39;49m[30;43m,[39;49m[30;43m [39;49m[30;43mprotocol[39;49m[30;43m [39;49m[30;43m+[39;49m
[32m    537[39m [30;43m                          [39;49m[30;43m'[39;49m[30;43m_open[39;49m[30;43m'[39;49m[30;43m,[39;49m[30;43m [39;49m[30;43mreq[39;49m[30;43m)[39;49m
[32m    538[39m [38;5;28;01mif[39;00m result:
[32m    539[39m     [38;5;28;01mreturn[39;00m result

[36mFile [39m[32m/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/urllib/request.py:496[39m, in [36mOpenerDirector._call_chain[39m[34m(self, chain, kind, meth_name, *args)[39m
[32m    494[39m [38;5;28;01mfor[39;00m handler [38;5;129;01min[39;00m handlers:
[32m    495[39m     func = [38;5;28mgetattr[39m(handler, meth_name)
[32m--> [39m[32m496[39m     result = [30;43mfunc[39;49m[30;43m([39;49m[30;43m*[39;49m[30;43margs[39;49m[30;43m)[39;49m
[32m    497[39m     [38;5;28;01mif[39;00m result [38;5;129;01mis[39;00m [38;5;129;01mnot[39;00m [38;5;28;01mNone[39;00m:
[32m    498[39m         [38;5;28;01mreturn[39;00m result

[36mFile [39m[32m/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/urllib/request.py:1391[39m, in [36mHTTPSHandler.https_open[39m[34m(self, req)[39m
[32m   1390[39m [38;5;28;01mdef[39;00m[38;5;250m [39m[34mhttps_open[39m([38;5;28mself[39m, req):
[32m-> [39m[32m1391[39m     [38;5;28;01mreturn[39;00m [30;43mself[39;49m[30;43m.[39;49m[30;43mdo_open[39;49m[30;43m([39;49m[30;43mhttp[39;49m[30;43m.[39;49m[30;43mclient[39;49m[30;43m.[39;49m[30;43mHTTPSConnection[39;49m[30;43m,[39;49m[30;43m [39;49m[30;43mreq[39;49m[30;43m,[39;49m
[32m   1392[39m [30;43m        [39;49m[30;43mcontext[39;49m[30;43m=[39;49m[30;43mself[39;49m[30;43m.[39;49m[30;43m_context[39;49m[30;43m,[39;49m[30;43m [39;49m[30;43mcheck_hostname[39;49m[30;43m=[39;49m[30;43mself[39;49m[30;43m.[39;49m[30;43m_check_hostname[39;49m[30;43m)[39;49m

[36mFile [39m[32m/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/urllib/request.py:1351[39m, in [36mAbstractHTTPHandler.do_open[39m[34m(self, http_class, req, **http_conn_args)[39m
[32m   1348[39m         h.request(req.get_method(), req.selector, req.data, headers,
[32m   1349[39m                   encode_chunked=req.has_header([33m'[39m[33mTransfer-encoding[39m[33m'[39m))
[32m   1350[39m     [38;5;28;01mexcept[39;00m [38;5;167;01mOSError[39;00m [38;5;28;01mas[39;00m err: [38;5;66;03m# timeout error[39;00m
[32m-> [39m[32m1351[39m         [38;5;28;01mraise[39;00m URLError(err)
[32m   1352[39m     r = h.getresponse()
[32m   1353[39m [38;5;28;01mexcept[39;00m:

[31mURLError[39m: <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1006)>


```

### `Chapter02/transfer_learning_alexnet.ipynb`
```
Traceback (most recent call last):
  File "/Users/ashish/code/MasteringPyTorchV3/scripts/validate_notebooks.py", line 85, in run_one
    client.execute()
  File "/Users/ashish/code/MasteringPyTorchV3/.venv/lib/python3.11/site-packages/jupyter_core/utils/__init__.py", line 165, in wrapped
    return loop.run_until_complete(inner)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/asyncio/base_events.py", line 654, in run_until_complete
    return future.result()
           ^^^^^^^^^^^^^^^
  File "/Users/ashish/code/MasteringPyTorchV3/.venv/lib/python3.11/site-packages/nbclient/client.py", line 709, in async_execute
    await self.async_execute_cell(
  File "/Users/ashish/code/MasteringPyTorchV3/.venv/lib/python3.11/site-packages/nbclient/client.py", line 1062, in async_execute_cell
    await self._check_raise_for_error(cell, cell_index, exec_reply)
  File "/Users/ashish/code/MasteringPyTorchV3/.venv/lib/python3.11/site-packages/nbclient/client.py", line 918, in _check_raise_for_error
    raise CellExecutionError.from_cell_and_msg(cell, exec_reply_content)
nbclient.exceptions.CellExecutionError: An error occurred while executing the following cell:
------------------
ddir = 'hymenoptera_data'

# Data normalization and augmentation transformations for train dataset
# Only normalization transformation for validation dataset
# The mean and std for normalization are calculated as the mean of all pixel values for all images in the training set per each image channel - R, G and B

data_transformers = {
    'train': transforms.Compose([transforms.RandomResizedCrop(224), transforms.RandomHorizontalFlip(),
                                    transforms.ToTensor(), 
                                    transforms.Normalize([0.490, 0.449, 0.411], [0.231, 0.221, 0.230])]),
    'val': transforms.Compose([transforms.Resize(256), transforms.CenterCrop(224), 
                                      transforms.ToTensor(), 
                                      transforms.Normalize([0.490, 0.449, 0.411], [0.231, 0.221, 0.230])])}

img_data = {k: datasets.ImageFolder(os.path.join(ddir, k), data_transformers[k]) for k in ['train', 'val']}
dloaders = {k: torch.utils.data.DataLoader(img_data[k], batch_size=8, shuffle=True) 
            for k in ['train', 'val']}
dset_sizes = {x: len(img_data[x]) for x in ['train', 'val']}
classes = img_data['train'].classes
dvc = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
------------------


[31m---------------------------------------------------------------------------[39m
[31mFileNotFoundError[39m                         Traceback (most recent call last)
[36mCell[39m[36m [39m[32mIn[3][39m[32m, line 15[39m
[32m     11[39m     'val': transforms.Compose([transforms.Resize(256), transforms.CenterCrop(224), 
[32m     12[39m                                       transforms.ToTensor(),
[32m     13[39m                                       transforms.Normalize([0.490, 0.449, 0.411], [0.231, 0.221, 0.230])])}
[32m     14[39m 
[32m---> [39m[32m15[39m img_data = {k: datasets.ImageFolder(os.path.join(ddir, k), data_transformers[k]) [38;5;28;01mfor[39;00m k [38;5;28;01min[39;00m [[33m'train'[39m, [33m'val'[39m]}
[32m     16[39m dloaders = {k: torch.utils.data.DataLoader(img_data[k], batch_size=8, shuffle=True) 
[32m     17[39m             for k in ['train', 'val']}
[32m     18[39m dset_sizes = {x: len(img_data[x]) [38;5;28;01mfor[39;00m x [38;5;28;01min[39;00m [[33m'train'[39m, [33m'val'[39m]}

[36mCell[39m[36m [39m[32mIn[3][39m[32m, line 15[39m, in [36m<dictcomp>[39m[34m(.0)[39m
[32m---> [39m[32m15[39m ddir = [33m'hymenoptera_data'[39m

[36mFile [39m[32m~/code/MasteringPyTorchV3/.venv/lib/python3.11/site-packages/torchvision/datasets/folder.py:328[39m, in [36mImageFolder.__init__[39m[34m(self, root, transform, target_transform, loader, is_valid_file, allow_empty)[39m
[32m    319[39m [38;5;28;01mdef[39;00m[38;5;250m [39m[34m__init__[39m(
[32m    320[39m     [38;5;28mself[39m,
[32m    321[39m     root: Union[[38;5;28mstr[39m, Path],
[32m   (...)[39m[32m    326[39m     allow_empty: [38;5;28mbool[39m = [38;5;28;01mFalse[39;00m,
[32m    327[39m ):
[32m--> [39m[32m328[39m     [30;43msuper[39;49m[30;43m([39;49m[30;43m)[39;49m[30;43m.[39;49m[30;43m__init__[39;49m[30;43m([39;49m
[32m    329[39m [30;43m        [39;49m[30;43mroot[39;49m[30;43m,[39;49m
[32m    330[39m [30;43m        [39;49m[30;43mloader[39;49m[30;43m,[39;49m
[32m    331[39m [30;43m        [39;49m[30;43mIMG_EXTENSIONS[39;49m[30;43m [39;49m[30;43;01mif[39;49;00m[30;43m [39;49m[30;43mis_valid_file[39;49m[30;43m [39;49m[30;43;01mis[39;49;00m[30;43m [39;49m[30;43;01mNone[39;49;00m[30;43m [39;49m[30;43;01melse[39;49;00m[30;43m [39;49m[30;43;01mNone[39;49;00m[30;43m,[39;49m
[32m    332[39m [30;43m        [39;49m[30;43mtransform[39;49m[30;43m=[39;49m[30;43mtransform[39;49m[30;43m,[39;49m
[32m    333[39m [30;43m        [39;49m[30;43mtarget_transform[39;49m[30;43m=[39;49m[30;43mtarget_transform[39;49m[30;43m,[39;49m
[32m    334[39m [30;43m        [39;49m[30;43mis_valid_file[39;49m[30;43m=[39;49m[30;43mis_valid_file[39;49m[30;43m,[39;49m
[32m    335[39m [30;43m        [39;49m[30;43mallow_empty[39;49m[30;43m=[39;49m[30;43mallow_empty[39;49m[30;43m,[39;49m
[32m    336[39m [30;43m    [39;49m[30;43m)[39;49m
[32m    337[39m     [38;5;28mself[39m.imgs = [38;5;28mself[39m.samples

[36mFile [39m[32m~/code/MasteringPyTorchV3/.venv/lib/python3.11/site-packages/torchvision/datasets/folder.py:149[39m, in [36mDatasetFolder.__init__[39m[34m(self, root, loader, extensions, transform, target_transform, is_valid_file, allow_empty)[39m
[32m    138[39m [38;5;28;01mdef[39;00m[38;5;250m [39m[34m__init__[39m(
[32m    139[39m     [38;5;28mself[39m,
[32m    140[39m     root: Union[[38;5;28mstr[39m, Path],
[32m   (...)[39m[32m    146[39m     allow_empty: [38;5;28mbool[39m = [38;5;28;01mFalse[39;00m,
[32m    147[39m ) -> [38;5;28;01mNone[39;00m:
[32m    148[39m     [38;5;28msuper[39m().[34m__init__[39m(root, transform=transform, target_transform=target_transform)
[32m--> [39m[32m149[39m     classes, class_to_idx = [30;43mself[39;49m[30;43m.[39;49m[30;43mfind_classes[39;49m[30;43m([39;49m[30;43mself[39;49m[30;43m.[39;49m[30;43mroot[39;49m[30;43m)[39;49m
[32m    150[39m     samples = [38;5;28mself[39m.make_dataset(
[32m    151[39m         [38;5;28mself[39m.root,
[32m    152[39m         class_to_idx=class_to_idx,
[32m   (...)[39m[32m    155[39m         allow_empty=allow_empty,
[32m    156[39m     )
[32m    158[39m     [38;5;28mself[39m.loader = loader

[36mFile [39m[32m~/code/MasteringPyTorchV3/.venv/lib/python3.11/site-packages/torchvision/datasets/folder.py:234[39m, in [36mDatasetFolder.find_classes[39m[34m(self, directory)[39m
[32m    207[39m [38;5;28;01mdef[39;00m[38;5;250m [39m[34mfind_classes[39m([38;5;28mself[39m, directory: Union[[38;5;28mstr[39m, Path]) -> [38;5;28mtuple[39m[[38;5;28mlist[39m[[38;5;28mstr[39m], [38;5;28mdict[39m[[38;5;28mstr[39m, [38;5;28mint[39m]]:
[32m    208[39m [38;5;250m    [39m[33;03m"""Find the class folders in a dataset structured as follows::[39;00m
[32m    209[39m 
[32m    210[39m [33;03m        directory/[39;00m
[32m   (...)[39m[32m    232[39m [33;03m        (Tuple[List[str], Dict[str, int]]): List of all classes and dictionary mapping each class to an index.[39;00m
[32m    233[39m [33;03m    """[39;00m
[32m--> [39m[32m234[39m     [38;5;28;01mreturn[39;00m [30;43mfind_classes[39;49m[30;43m([39;49m[30;43mdirectory[39;49m[30;43m)[39;49m

[36mFile [39m[32m~/code/MasteringPyTorchV3/.venv/lib/python3.11/site-packages/torchvision/datasets/folder.py:41[39m, in [36mfind_classes[39m[34m(directory)[39m
[32m     36[39m [38;5;28;01mdef[39;00m[38;5;250m [39m[34mfind_classes[39m(directory: Union[[38;5;28mstr[39m, Path]) -> [38;5;28mtuple[39m[[38;5;28mlist[39m[[38;5;28mstr[39m], [38;5;28mdict[39m[[38;5;28mstr[39m, [38;5;28mint[39m]]:
[32m     37[39m [38;5;250m    [39m[33;03m"""Finds the class folders in a dataset.[39;00m
[32m     38[39m 
[32m     39[39m [33;03m    See :class:`DatasetFolder` for details.[39;00m
[32m     40[39m [33;03m    """[39;00m
[32m---> [39m[32m41[39m     classes = [38;5;28msorted[39m(entry.name [38;5;28;01mfor[39;00m entry [38;5;129;01min[39;00m [30;43mos[39;49m[30;43m.[39;49m[30;43mscandir[39;49m[30;43m([39;49m[30;43mdirectory[39;49m[30;43m)[39;49m [38;5;28;01mif[39;00m entry.is_dir())
[32m     42[39m     [38;5;28;01mif[39;00m [38;5;129;01mnot[39;00m classes:
[32m     43[39m         [38;5;28;01mraise[39;00m [38;5;167;01mFileNotFoundError[39;00m([33mf[39m[33m"[39m[33mCouldn[39m[33m'[39m[33mt find any class folder in [39m[38;5;132;01m{[39;00mdirectory[38;5;132;01m}[39;00m[33m.[39m[33m"[39m)

[31mFileNotFoundError[39m: [Errno 2] No such file or directory: 'hymenoptera_data/train'


```

### `Chapter02/vgg13_pretrained_run_inference.ipynb`
```
Traceback (most recent call last):
  File "/Users/ashish/code/MasteringPyTorchV3/scripts/validate_notebooks.py", line 85, in run_one
    client.execute()
  File "/Users/ashish/code/MasteringPyTorchV3/.venv/lib/python3.11/site-packages/jupyter_core/utils/__init__.py", line 165, in wrapped
    return loop.run_until_complete(inner)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/asyncio/base_events.py", line 654, in run_until_complete
    return future.result()
           ^^^^^^^^^^^^^^^
  File "/Users/ashish/code/MasteringPyTorchV3/.venv/lib/python3.11/site-packages/nbclient/client.py", line 709, in async_execute
    await self.async_execute_cell(
  File "/Users/ashish/code/MasteringPyTorchV3/.venv/lib/python3.11/site-packages/nbclient/client.py", line 1062, in async_execute_cell
    await self._check_raise_for_error(cell, cell_index, exec_reply)
  File "/Users/ashish/code/MasteringPyTorchV3/.venv/lib/python3.11/site-packages/nbclient/client.py", line 918, in _check_raise_for_error
    raise CellExecutionError.from_cell_and_msg(cell, exec_reply_content)
nbclient.exceptions.CellExecutionError: An error occurred while executing the following cell:
------------------
ddir = 'hymenoptera_data'

# Data normalization and augmentation transformations for train dataset
# Only normalization transformation for validation dataset

data_transformers = {
    'train': transforms.Compose([transforms.RandomResizedCrop(224), transforms.RandomHorizontalFlip(),
                                    transforms.ToTensor(), 
                                    transforms.Normalize([0.490, 0.449, 0.411], [0.231, 0.221, 0.230])]),
    'val': transforms.Compose([transforms.Resize(256), transforms.CenterCrop(224), 
                                      transforms.ToTensor(), 
                                      transforms.Normalize([0.490, 0.449, 0.411], [0.231, 0.221, 0.230])])}

img_data = {k: datasets.ImageFolder(os.path.join(ddir, k), data_transformers[k]) for k in ['train', 'val']}
dloaders = {k: torch.utils.data.DataLoader(img_data[k], batch_size=8, shuffle=True, num_workers=2) 
            for k in ['train', 'val']}
dset_sizes = {x: len(img_data[x]) for x in ['train', 'val']}
dvc = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
------------------


[31m---------------------------------------------------------------------------[39m
[31mFileNotFoundError[39m                         Traceback (most recent call last)
[36mCell[39m[36m [39m[32mIn[3][39m[32m, line 14[39m
[32m     10[39m     'val': transforms.Compose([transforms.Resize(256), transforms.CenterCrop(224), 
[32m     11[39m                                       transforms.ToTensor(),
[32m     12[39m                                       transforms.Normalize([0.490, 0.449, 0.411], [0.231, 0.221, 0.230])])}
[32m     13[39m 
[32m---> [39m[32m14[39m img_data = {k: datasets.ImageFolder(os.path.join(ddir, k), data_transformers[k]) [38;5;28;01mfor[39;00m k [38;5;28;01min[39;00m [[33m'train'[39m, [33m'val'[39m]}
[32m     15[39m dloaders = {k: torch.utils.data.DataLoader(img_data[k], batch_size=8, shuffle=True, num_workers=2) 
[32m     16[39m             for k in ['train', 'val']}
[32m     17[39m dset_sizes = {x: len(img_data[x]) [38;5;28;01mfor[39;00m x [38;5;28;01min[39;00m [[33m'train'[39m, [33m'val'[39m]}

[36mCell[39m[36m [39m[32mIn[3][39m[32m, line 14[39m, in [36m<dictcomp>[39m[34m(.0)[39m
[32m---> [39m[32m14[39m ddir = [33m'hymenoptera_data'[39m

[36mFile [39m[32m~/code/MasteringPyTorchV3/.venv/lib/python3.11/site-packages/torchvision/datasets/folder.py:328[39m, in [36mImageFolder.__init__[39m[34m(self, root, transform, target_transform, loader, is_valid_file, allow_empty)[39m
[32m    319[39m [38;5;28;01mdef[39;00m[38;5;250m [39m[34m__init__[39m(
[32m    320[39m     [38;5;28mself[39m,
[32m    321[39m     root: Union[[38;5;28mstr[39m, Path],
[32m   (...)[39m[32m    326[39m     allow_empty: [38;5;28mbool[39m = [38;5;28;01mFalse[39;00m,
[32m    327[39m ):
[32m--> [39m[32m328[39m     [30;43msuper[39;49m[30;43m([39;49m[30;43m)[39;49m[30;43m.[39;49m[30;43m__init__[39;49m[30;43m([39;49m
[32m    329[39m [30;43m        [39;49m[30;43mroot[39;49m[30;43m,[39;49m
[32m    330[39m [30;43m        [39;49m[30;43mloader[39;49m[30;43m,[39;49m
[32m    331[39m [30;43m        [39;49m[30;43mIMG_EXTENSIONS[39;49m[30;43m [39;49m[30;43;01mif[39;49;00m[30;43m [39;49m[30;43mis_valid_file[39;49m[30;43m [39;49m[30;43;01mis[39;49;00m[30;43m [39;49m[30;43;01mNone[39;49;00m[30;43m [39;49m[30;43;01melse[39;49;00m[30;43m [39;49m[30;43;01mNone[39;49;00m[30;43m,[39;49m
[32m    332[39m [30;43m        [39;49m[30;43mtransform[39;49m[30;43m=[39;49m[30;43mtransform[39;49m[30;43m,[39;49m
[32m    333[39m [30;43m        [39;49m[30;43mtarget_transform[39;49m[30;43m=[39;49m[30;43mtarget_transform[39;49m[30;43m,[39;49m
[32m    334[39m [30;43m        [39;49m[30;43mis_valid_file[39;49m[30;43m=[39;49m[30;43mis_valid_file[39;49m[30;43m,[39;49m
[32m    335[39m [30;43m        [39;49m[30;43mallow_empty[39;49m[30;43m=[39;49m[30;43mallow_empty[39;49m[30;43m,[39;49m
[32m    336[39m [30;43m    [39;49m[30;43m)[39;49m
[32m    337[39m     [38;5;28mself[39m.imgs = [38;5;28mself[39m.samples

[36mFile [39m[32m~/code/MasteringPyTorchV3/.venv/lib/python3.11/site-packages/torchvision/datasets/folder.py:149[39m, in [36mDatasetFolder.__init__[39m[34m(self, root, loader, extensions, transform, target_transform, is_valid_file, allow_empty)[39m
[32m    138[39m [38;5;28;01mdef[39;00m[38;5;250m [39m[34m__init__[39m(
[32m    139[39m     [38;5;28mself[39m,
[32m    140[39m     root: Union[[38;5;28mstr[39m, Path],
[32m   (...)[39m[32m    146[39m     allow_empty: [38;5;28mbool[39m = [38;5;28;01mFalse[39;00m,
[32m    147[39m ) -> [38;5;28;01mNone[39;00m:
[32m    148[39m     [38;5;28msuper[39m().[34m__init__[39m(root, transform=transform, target_transform=target_transform)
[32m--> [39m[32m149[39m     classes, class_to_idx = [30;43mself[39;49m[30;43m.[39;49m[30;43mfind_classes[39;49m[30;43m([39;49m[30;43mself[39;49m[30;43m.[39;49m[30;43mroot[39;49m[30;43m)[39;49m
[32m    150[39m     samples = [38;5;28mself[39m.make_dataset(
[32m    151[39m         [38;5;28mself[39m.root,
[32m    152[39m         class_to_idx=class_to_idx,
[32m   (...)[39m[32m    155[39m         allow_empty=allow_empty,
[32m    156[39m     )
[32m    158[39m     [38;5;28mself[39m.loader = loader

[36mFile [39m[32m~/code/MasteringPyTorchV3/.venv/lib/python3.11/site-packages/torchvision/datasets/folder.py:234[39m, in [36mDatasetFolder.find_classes[39m[34m(self, directory)[39m
[32m    207[39m [38;5;28;01mdef[39;00m[38;5;250m [39m[34mfind_classes[39m([38;5;28mself[39m, directory: Union[[38;5;28mstr[39m, Path]) -> [38;5;28mtuple[39m[[38;5;28mlist[39m[[38;5;28mstr[39m], [38;5;28mdict[39m[[38;5;28mstr[39m, [38;5;28mint[39m]]:
[32m    208[39m [38;5;250m    [39m[33;03m"""Find the class folders in a dataset structured as follows::[39;00m
[32m    209[39m 
[32m    210[39m [33;03m        directory/[39;00m
[32m   (...)[39m[32m    232[39m [33;03m        (Tuple[List[str], Dict[str, int]]): List of all classes and dictionary mapping each class to an index.[39;00m
[32m    233[39m [33;03m    """[39;00m
[32m--> [39m[32m234[39m     [38;5;28;01mreturn[39;00m [30;43mfind_classes[39;49m[30;43m([39;49m[30;43mdirectory[39;49m[30;43m)[39;49m

[36mFile [39m[32m~/code/MasteringPyTorchV3/.venv/lib/python3.11/site-packages/torchvision/datasets/folder.py:41[39m, in [36mfind_classes[39m[34m(directory)[39m
[32m     36[39m [38;5;28;01mdef[39;00m[38;5;250m [39m[34mfind_classes[39m(directory: Union[[38;5;28mstr[39m, Path]) -> [38;5;28mtuple[39m[[38;5;28mlist[39m[[38;5;28mstr[39m], [38;5;28mdict[39m[[38;5;28mstr[39m, [38;5;28mint[39m]]:
[32m     37[39m [38;5;250m    [39m[33;03m"""Finds the class folders in a dataset.[39;00m
[32m     38[39m 
[32m     39[39m [33;03m    See :class:`DatasetFolder` for details.[39;00m
[32m     40[39m [33;03m    """[39;00m
[32m---> [39m[32m41[39m     classes = [38;5;28msorted[39m(entry.name [38;5;28;01mfor[39;00m entry [38;5;129;01min[39;00m [30;43mos[39;49m[30;43m.[39;49m[30;43mscandir[39;49m[30;43m([39;49m[30;43mdirectory[39;49m[30;43m)[39;49m [38;5;28;01mif[39;00m entry.is_dir())
[32m     42[39m     [38;5;28;01mif[39;00m [38;5;129;01mnot[39;00m classes:
[32m     43[39m         [38;5;28;01mraise[39;00m [38;5;167;01mFileNotFoundError[39;00m([33mf[39m[33m"[39m[33mCouldn[39m[33m'[39m[33mt find any class folder in [39m[38;5;132;01m{[39;00mdirectory[38;5;132;01m}[39;00m[33m.[39m[33m"[39m)

[31mFileNotFoundError[39m: [Errno 2] No such file or directory: 'hymenoptera_data/train'


```

### `Chapter03/rnn.ipynb`
```
Traceback (most recent call last):
  File "/Users/ashish/code/MasteringPyTorchV3/scripts/validate_notebooks.py", line 85, in run_one
    client.execute()
  File "/Users/ashish/code/MasteringPyTorchV3/.venv/lib/python3.11/site-packages/jupyter_core/utils/__init__.py", line 165, in wrapped
    return loop.run_until_complete(inner)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/asyncio/base_events.py", line 654, in run_until_complete
    return future.result()
           ^^^^^^^^^^^^^^^
  File "/Users/ashish/code/MasteringPyTorchV3/.venv/lib/python3.11/site-packages/nbclient/client.py", line 709, in async_execute
    await self.async_execute_cell(
  File "/Users/ashish/code/MasteringPyTorchV3/.venv/lib/python3.11/site-packages/nbclient/client.py", line 1062, in async_execute_cell
    await self._check_raise_for_error(cell, cell_index, exec_reply)
  File "/Users/ashish/code/MasteringPyTorchV3/.venv/lib/python3.11/site-packages/nbclient/client.py", line 918, in _check_raise_for_error
    raise CellExecutionError.from_cell_and_msg(cell, exec_reply_content)
nbclient.exceptions.CellExecutionError: An error occurred while executing the following cell:
------------------
# read sentiments and reviews data from the text files
review_list = []
label_list = []
for label in ['pos', 'neg']:
    for fname in tqdm(os.listdir(f'./aclImdb/train/{label}/')):
        if 'txt' not in fname:
            continue
        with open(os.path.join(f'./aclImdb/train/{label}/', fname), encoding="utf8") as f:
            review_list += [f.read()]
            label_list += [label]
print ('Number of reviews :', len(review_list))
------------------


[31m---------------------------------------------------------------------------[39m
[31mFileNotFoundError[39m                         Traceback (most recent call last)
[36mCell[39m[36m [39m[32mIn[3][39m[32m, line 5[39m
[32m      1[39m [38;5;66;03m# read sentiments and reviews data from the text files[39;00m
[32m      2[39m review_list = []
[32m      3[39m label_list = []
[32m      4[39m [38;5;28;01mfor[39;00m label [38;5;28;01min[39;00m [[33m'pos'[39m, [33m'neg'[39m]:
[32m----> [39m[32m5[39m     [38;5;28;01mfor[39;00m fname [38;5;28;01min[39;00m tqdm(os.listdir([33mf'./aclImdb/train/{label}/'[39m)):
[32m      6[39m         [38;5;28;01mif[39;00m [33m'txt'[39m [38;5;28;01mnot[39;00m [38;5;28;01min[39;00m fname:
[32m      7[39m             [38;5;28;01mcontinue[39;00m
[32m      8[39m         [38;5;28;01mwith[39;00m open(os.path.join([33mf'./aclImdb/train/{label}/'[39m, fname), encoding=[33m"utf8"[39m) [38;5;28;01mas[39;00m f:

[31mFileNotFoundError[39m: [Errno 2] No such file or directory: './aclImdb/train/pos/'


```

### `Chapter03/lstm.ipynb`
```
Traceback (most recent call last):
  File "/Users/ashish/code/MasteringPyTorchV3/scripts/validate_notebooks.py", line 85, in run_one
    client.execute()
  File "/Users/ashish/code/MasteringPyTorchV3/.venv/lib/python3.11/site-packages/jupyter_core/utils/__init__.py", line 165, in wrapped
    return loop.run_until_complete(inner)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/asyncio/base_events.py", line 654, in run_until_complete
    return future.result()
           ^^^^^^^^^^^^^^^
  File "/Users/ashish/code/MasteringPyTorchV3/.venv/lib/python3.11/site-packages/nbclient/client.py", line 709, in async_execute
    await self.async_execute_cell(
  File "/Users/ashish/code/MasteringPyTorchV3/.venv/lib/python3.11/site-packages/nbclient/client.py", line 1062, in async_execute_cell
    await self._check_raise_for_error(cell, cell_index, exec_reply)
  File "/Users/ashish/code/MasteringPyTorchV3/.venv/lib/python3.11/site-packages/nbclient/client.py", line 918, in _check_raise_for_error
    raise CellExecutionError.from_cell_and_msg(cell, exec_reply_content)
nbclient.exceptions.CellExecutionError: An error occurred while executing the following cell:
------------------
import random
from torchtext.legacy import datasets
from torchtext.legacy import data
------------------


[31m---------------------------------------------------------------------------[39m
[31mModuleNotFoundError[39m                       Traceback (most recent call last)
[36mCell[39m[36m [39m[32mIn[3][39m[32m, line 2[39m
[32m      1[39m [38;5;28;01mimport[39;00m random
[32m----> [39m[32m2[39m [38;5;28;01mfrom[39;00m torchtext.legacy [38;5;28;01mimport[39;00m datasets
[32m      3[39m [38;5;28;01mfrom[39;00m torchtext.legacy [38;5;28;01mimport[39;00m data

[31mModuleNotFoundError[39m: No module named 'torchtext'


```

### `Chapter15/fastai.ipynb`
```
Traceback (most recent call last):
  File "/Users/ashish/code/MasteringPyTorchV3/scripts/validate_notebooks.py", line 85, in run_one
    client.execute()
  File "/Users/ashish/code/MasteringPyTorchV3/.venv/lib/python3.11/site-packages/jupyter_core/utils/__init__.py", line 165, in wrapped
    return loop.run_until_complete(inner)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/asyncio/base_events.py", line 654, in run_until_complete
    return future.result()
           ^^^^^^^^^^^^^^^
  File "/Users/ashish/code/MasteringPyTorchV3/.venv/lib/python3.11/site-packages/nbclient/client.py", line 709, in async_execute
    await self.async_execute_cell(
  File "/Users/ashish/code/MasteringPyTorchV3/.venv/lib/python3.11/site-packages/nbclient/client.py", line 1062, in async_execute_cell
    await self._check_raise_for_error(cell, cell_index, exec_reply)
  File "/Users/ashish/code/MasteringPyTorchV3/.venv/lib/python3.11/site-packages/nbclient/client.py", line 918, in _check_raise_for_error
    raise CellExecutionError.from_cell_and_msg(cell, exec_reply_content)
nbclient.exceptions.CellExecutionError: An error occurred while executing the following cell:
------------------
path = untar_data(URLs.MNIST)
print(path)
------------------


[31m---------------------------------------------------------------------------[39m
[31mSSLCertVerificationError[39m                  Traceback (most recent call last)
[36mFile [39m[32m/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/urllib/request.py:1348[39m, in [36mAbstractHTTPHandler.do_open[39m[34m(self, http_class, req, **http_conn_args)[39m
[32m   1347[39m [38;5;28;01mtry[39;00m:
[32m-> [39m[32m1348[39m     [30;43mh[39;49m[30;43m.[39;49m[30;43mrequest[39;49m[30;43m([39;49m[30;43mreq[39;49m[30;43m.[39;49m[30;43mget_method[39;49m[30;43m([39;49m[30;43m)[39;49m[30;43m,[39;49m[30;43m [39;49m[30;43mreq[39;49m[30;43m.[39;49m[30;43mselector[39;49m[30;43m,[39;49m[30;43m [39;49m[30;43mreq[39;49m[30;43m.[39;49m[30;43mdata[39;49m[30;43m,[39;49m[30;43m [39;49m[30;43mheaders[39;49m[30;43m,[39;49m
[32m   1349[39m [30;43m              [39;49m[30;43mencode_chunked[39;49m[30;43m=[39;49m[30;43mreq[39;49m[30;43m.[39;49m[30;43mhas_header[39;49m[30;43m([39;49m[30;43m'[39;49m[30;43mTransfer-encoding[39;49m[30;43m'[39;49m[30;43m)[39;49m[30;43m)[39;49m
[32m   1350[39m [38;5;28;01mexcept[39;00m [38;5;167;01mOSError[39;00m [38;5;28;01mas[39;00m err: [38;5;66;03m# timeout error[39;00m

[36mFile [39m[32m/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/http/client.py:1303[39m, in [36mHTTPConnection.request[39m[34m(self, method, url, body, headers, encode_chunked)[39m
[32m   1302[39m [38;5;250m[39m[33;03m"""Send a complete request to the server."""[39;00m
[32m-> [39m[32m1303[39m [30;43mself[39;49m[30;43m.[39;49m[30;43m_send_request[39;49m[30;43m([39;49m[30;43mmethod[39;49m[30;43m,[39;49m[30;43m [39;49m[30;43murl[39;49m[30;43m,[39;49m[30;43m [39;49m[30;43mbody[39;49m[30;43m,[39;49m[30;43m [39;49m[30;43mheaders[39;49m[30;43m,[39;49m[30;43m [39;49m[30;43mencode_chunked[39;49m[30;43m)[39;49m

[36mFile [39m[32m/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/http/client.py:1349[39m, in [36mHTTPConnection._send_request[39m[34m(self, method, url, body, headers, encode_chunked)[39m
[32m   1348[39m     body = _encode(body, [33m'[39m[33mbody[39m[33m'[39m)
[32m-> [39m[32m1349[39m [30;43mself[39;49m[30;43m.[39;49m[30;43mendheaders[39;49m[30;43m([39;49m[30;43mbody[39;49m[30;43m,[39;49m[30;43m [39;49m[30;43mencode_chunked[39;49m[30;43m=[39;49m[30;43mencode_chunked[39;49m[30;43m)[39;49m

[36mFile [39m[32m/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/http/client.py:1298[39m, in [36mHTTPConnection.endheaders[39m[34m(self, message_body, encode_chunked)[39m
[32m   1297[39m     [38;5;28;01mraise[39;00m CannotSendHeader()
[32m-> [39m[32m1298[39m [30;43mself[39;49m[30;43m.[39;49m[30;43m_send_output[39;49m[30;43m([39;49m[30;43mmessage_body[39;49m[30;43m,[39;49m[30;43m [39;49m[30;43mencode_chunked[39;49m[30;43m=[39;49m[30;43mencode_chunked[39;49m[30;43m)[39;49m

[36mFile [39m[32m/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/http/client.py:1058[39m, in [36mHTTPConnection._send_output[39m[34m(self, message_body, encode_chunked)[39m
[32m   1057[39m [38;5;28;01mdel[39;00m [38;5;28mself[39m._buffer[:]
[32m-> [39m[32m1058[39m [30;43mself[39;49m[30;43m.[39;49m[30;43msend[39;49m[30;43m([39;49m[30;43mmsg[39;49m[30;43m)[39;49m
[32m   1060[39m [38;5;28;01mif[39;00m message_body [38;5;129;01mis[39;00m [38;5;129;01mnot[39;00m [38;5;28;01mNone[39;00m:
[32m   1061[39m 
[32m   1062[39m     [38;5;66;03m# create a consistent interface to message_body[39;00m

[36mFile [39m[32m/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/http/client.py:996[39m, in [36mHTTPConnection.send[39m[34m(self, data)[39m
[32m    995[39m [38;5;28;01mif[39;00m [38;5;28mself[39m.auto_open:
[32m--> [39m[32m996[39m     [30;43mself[39;49m[30;43m.[39;49m[30;43mconnect[39;49m[30;43m([39;49m[30;43m)[39;49m
[32m    997[39m [38;5;28;01melse[39;00m:

[36mFile [39m[32m/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/http/client.py:1475[39m, in [36mHTTPSConnection.connect[39m[34m(self)[39m
[32m   1473[39m     server_hostname = [38;5;28mself[39m.host
[32m-> [39m[32m1475[39m [38;5;28mself[39m.sock = [30;43mself[39;49m[30;43m.[39;49m[30;43m_context[39;49m[30;43m.[39;49m[30;43mwrap_socket[39;49m[30;43m([39;49m[30;43mself[39;49m[30;43m.[39;49m[30;43msock[39;49m[30;43m,[39;49m
[32m   1476[39m [30;43m                                      [39;49m[30;43mserver_hostname[39;49m[30;43m=[39;49m[30;43mserver_hostname[39;49m[30;43m)[39;49m

[36mFile [39m[32m/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/ssl.py:517[39m, in [36mSSLContext.wrap_socket[39m[34m(self, sock, server_side, do_handshake_on_connect, suppress_ragged_eofs, server_hostname, session)[39m
[32m    511[39m [38;5;28;01mdef[39;00m[38;5;250m [39m[34mwrap_socket[39m([38;5;28mself[39m, sock, server_side=[38;5;28;01mFalse[39;00m,
[32m    512[39m                 do_handshake_on_connect=[38;5;28;01mTrue[39;00m,
[32m    513[39m                 suppress_ragged_eofs=[38;5;28;01mTrue[39;00m,
[32m    514[39m                 server_hostname=[38;5;28;01mNone[39;00m, session=[38;5;28;01mNone[39;00m):
[32m    515[39m     [38;5;66;03m# SSLSocket class handles server_hostname encoding before it calls[39;00m
[32m    516[39m     [38;5;66;03m# ctx._wrap_socket()[39;00m
[32m--> [39m[32m517[39m     [38;5;28;01mreturn[39;00m [30;43mself[39;49m[30;43m.[39;49m[30;43msslsocket_class[39;49m[30;43m.[39;49m[30;43m_create[39;49m[30;43m([39;49m
[32m    518[39m [30;43m        [39;49m[30;43msock[39;49m[30;43m=[39;49m[30;43msock[39;49m[30;43m,[39;49m
[32m    519[39m [30;43m        [39;49m[30;43mserver_side[39;49m[30;43m=[39;49m[30;43mserver_side[39;49m[30;43m,[39;49m
[32m    520[39m [30;43m        [39;49m[30;43mdo_handshake_on_connect[39;49m[30;43m=[39;49m[30;43mdo_handshake_on_connect[39;49m[30;43m,[39;49m
[32m    521[39m [30;43m        [39;49m[30;43msuppress_ragged_eofs[39;49m[30;43m=[39;49m[30;43msuppress_ragged_eofs[39;49m[30;43m,[39;49m
[32m    522[39m [30;43m        [39;49m[30;43mserver_hostname[39;49m[30;43m=[39;49m[30;43mserver_hostname[39;49m[30;43m,[39;49m
[32m    523[39m [30;43m        [39;49m[30;43mcontext[39;49m[30;43m=[39;49m[30;43mself[39;49m[30;43m,[39;49m
[32m    524[39m [30;43m        [39;49m[30;43msession[39;49m[30;43m=[39;49m[30;43msession[39;49m
[32m    525[39m [30;43m    [39;49m[30;43m)[39;49m

[36mFile [39m[32m/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/ssl.py:1104[39m, in [36mSSLSocket._create[39m[34m(cls, sock, server_side, do_handshake_on_connect, suppress_ragged_eofs, server_hostname, context, session)[39m
[32m   1103[39m                 [38;5;28;01mraise[39;00m [38;5;167;01mValueError[39;00m([33m"[39m[33mdo_handshake_on_connect should not be specified for non-blocking sockets[39m[33m"[39m)
[32m-> [39m[32m1104[39m             [30;43mself[39;49m[30;43m.[39;49m[30;43mdo_handshake[39;49m[30;43m([39;49m[30;43m)[39;49m
[32m   1105[39m [38;5;28;01mexcept[39;00m:

[36mFile [39m[32m/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/ssl.py:1382[39m, in [36mSSLSocket.do_handshake[39m[34m(self, block)[39m
[32m   1381[39m         [38;5;28mself[39m.settimeout([38;5;28;01mNone[39;00m)
[32m-> [39m[32m1382[39m     [30;43mself[39;49m[30;43m.[39;49m[30;43m_sslobj[39;49m[30;43m.[39;49m[30;43mdo_handshake[39;49m[30;43m([39;49m[30;43m)[39;49m
[32m   1383[39m [38;5;28;01mfinally[39;00m:

[31mSSLCertVerificationError[39m: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1006)

During handling of the above exception, another exception occurred:

[31mURLError[39m                                  Traceback (most recent call last)
[36mCell[39m[36m [39m[32mIn[3][39m[32m, line 1[39m
[32m----> [39m[32m1[39m path = untar_data(URLs.MNIST)
[32m      2[39m print(path)

[36mFile [39m[32m~/code/MasteringPyTorchV3/.venv/lib/python3.11/site-packages/fastai/data/external.py:145[39m, in [36muntar_data[39m[34m(url, archive, data, c_key, force_download, base)[39m
[32m    143[39m     base = [33m'[39m[33m~/.fastai[39m[33m'[39m
[32m    144[39m d = FastDownload(cfg, module=fastai.data, archive=archive, data=data, base=base)
[32m--> [39m[32m145[39m [38;5;28;01mreturn[39;00m [30;43md[39;49m[30;43m.[39;49m[30;43mget[39;49m[30;43m([39;49m[30;43murl[39;49m[30;43m,[39;49m[30;43m [39;49m[30;43mforce[39;49m[30;43m=[39;49m[30;43mforce_download[39;49m[30;43m,[39;49m[30;43m [39;49m[30;43mextract_key[39;49m[30;43m=[39;49m[30;43mc_key[39;49m[30;43m)[39;49m

[36mFile [39m[32m~/code/MasteringPyTorchV3/.venv/lib/python3.11/site-packages/fastdownload/core.py:117[39m, in [36mFastDownload.get[39m[34m(self, url, extract_key, force)[39m
[32m    115[39m     data = [38;5;28mself[39m.data_path(extract_key, urldest(url, [38;5;28mself[39m.arch_path()))
[32m    116[39m     [38;5;28;01mif[39;00m data.exists(): [38;5;28;01mreturn[39;00m data
[32m--> [39m[32m117[39m [30;43mself[39;49m[30;43m.[39;49m[30;43mdownload[39;49m[30;43m([39;49m[30;43murl[39;49m[30;43m,[39;49m[30;43m [39;49m[30;43mforce[39;49m[30;43m=[39;49m[30;43mforce[39;49m[30;43m)[39;49m
[32m    118[39m [38;5;28;01mreturn[39;00m [38;5;28mself[39m.extract(url, extract_key=extract_key, force=force)

[36mFile [39m[32m~/code/MasteringPyTorchV3/.venv/lib/python3.11/site-packages/fastdownload/core.py:92[39m, in [36mFastDownload.download[39m[34m(self, url, force)[39m
[32m     90[39m [33m"[39m[33mDownload `url` to archive path, unless exists and `self.check` fails and not `force`[39m[33m"[39m
[32m     91[39m [38;5;28mself[39m.arch_path().mkdir(exist_ok=[38;5;28;01mTrue[39;00m, parents=[38;5;28;01mTrue[39;00m)
[32m---> [39m[32m92[39m [38;5;28;01mreturn[39;00m [30;43mdownload_and_check[39;49m[30;43m([39;49m[30;43murl[39;49m[30;43m,[39;49m[30;43m [39;49m[30;43murldest[39;49m[30;43m([39;49m[30;43murl[39;49m[30;43m,[39;49m[30;43m [39;49m[30;43mself[39;49m[30;43m.[39;49m[30;43march_path[39;49m[30;43m([39;49m[30;43m)[39;49m[30;43m)[39;49m[30;43m,[39;49m[30;43m [39;49m[30;43mself[39;49m[30;43m.[39;49m[30;43mmodule[39;49m[30;43m,[39;49m[30;43m [39;49m[30;43mforce[39;49m[30;43m)[39;49m

[36mFile [39m[32m~/code/MasteringPyTorchV3/.venv/lib/python3.11/site-packages/fastdownload/core.py:61[39m, in [36mdownload_and_check[39m[34m(url, fpath, fmod, force)[39m
[32m     59[39m     [38;5;28;01mif[39;00m check(fmod, url, fpath): [38;5;28;01mreturn[39;00m fpath
[32m     60[39m     [38;5;28;01melse[39;00m: [38;5;28mprint[39m([33m"[39m[33mDownloading a new version of this dataset...[39m[33m"[39m)
[32m---> [39m[32m61[39m res = [30;43mdownload_url[39;49m[30;43m([39;49m[30;43murl[39;49m[30;43m,[39;49m[30;43m [39;49m[30;43mfpath[39;49m[30;43m)[39;49m
[32m     62[39m [38;5;28;01mif[39;00m [38;5;129;01mnot[39;00m check(fmod, url, fpath): [38;5;28;01mraise[39;00m [38;5;167;01mException[39;00m([33m"[39m[33mDownloaded file is corrupt or not latest version[39m[33m"[39m)
[32m     63[39m [38;5;28;01mreturn[39;00m res

[36mFile [39m[32m~/code/MasteringPyTorchV3/.venv/lib/python3.11/site-packages/fastdownload/core.py:19[39m, in [36mdownload_url[39m[34m(url, dest, timeout, show_progress)[39m
[32m     17[39m     pbar.total = tsize
[32m     18[39m     pbar.update(count*bsize)
[32m---> [39m[32m19[39m [38;5;28;01mreturn[39;00m [30;43murlsave[39;49m[30;43m([39;49m[30;43murl[39;49m[30;43m,[39;49m[30;43m [39;49m[30;43mdest[39;49m[30;43m,[39;49m[30;43m [39;49m[30;43mreporthook[39;49m[30;43m=[39;49m[30;43mprogress[39;49m[30;43m [39;49m[30;43;01mif[39;49;00m[30;43m [39;49m[30;43mshow_progress[39;49m[30;43m [39;49m[30;43;01melse[39;49;00m[30;43m [39;49m[30;43;01mNone[39;49;00m[30;43m,[39;49m[30;43m [39;49m[30;43mtimeout[39;49m[30;43m=[39;49m[30;43mtimeout[39;49m[30;43m)[39;49m

[36mFile [39m[32m~/code/MasteringPyTorchV3/.venv/lib/python3.11/site-packages/fastcore/net.py:186[39m, in [36murlsave[39m[34m(url, dest, reporthook, headers, timeout)[39m
[32m    184[39m dest = urldest(url, dest)
[32m    185[39m dest.parent.mkdir(parents=[38;5;28;01mTrue[39;00m, exist_ok=[38;5;28;01mTrue[39;00m)
[32m--> [39m[32m186[39m nm,msg = [30;43murlretrieve[39;49m[30;43m([39;49m[30;43murl[39;49m[30;43m,[39;49m[30;43m [39;49m[30;43mdest[39;49m[30;43m,[39;49m[30;43m [39;49m[30;43mreporthook[39;49m[30;43m,[39;49m[30;43m [39;49m[30;43mheaders[39;49m[30;43m=[39;49m[30;43mheaders[39;49m[30;43m,[39;49m[30;43m [39;49m[30;43mtimeout[39;49m[30;43m=[39;49m[30;43mtimeout[39;49m[30;43m)[39;49m
[32m    187[39m [38;5;28;01mreturn[39;00m nm

[36mFile [39m[32m~/code/MasteringPyTorchV3/.venv/lib/python3.11/site-packages/fastcore/net.py:152[39m, in [36murlretrieve[39m[34m(url, filename, reporthook, data, headers, timeout)[39m
[32m    150[39m [38;5;28;01mdef[39;00m[38;5;250m [39m[34murlretrieve[39m(url, filename=[38;5;28;01mNone[39;00m, reporthook=[38;5;28;01mNone[39;00m, data=[38;5;28;01mNone[39;00m, headers=[38;5;28;01mNone[39;00m, timeout=[38;5;28;01mNone[39;00m):
[32m    151[39m     [33m"[39m[33mSame as `urllib.request.urlretrieve` but also works with `Request` objects[39m[33m"[39m
[32m--> [39m[32m152[39m     [38;5;28;01mwith[39;00m contextlib.closing([30;43murlopen[39;49m[30;43m([39;49m[30;43murl[39;49m[30;43m,[39;49m[30;43m [39;49m[30;43mdata[39;49m[30;43m,[39;49m[30;43m [39;49m[30;43mheaders[39;49m[30;43m=[39;49m[30;43mheaders[39;49m[30;43m,[39;49m[30;43m [39;49m[30;43mtimeout[39;49m[30;43m=[39;49m[30;43mtimeout[39;49m[30;43m)[39;49m) [38;5;28;01mas[39;00m fp:
[32m    153[39m         headers = fp.info()
[32m    154[39m         [38;5;28;01mif[39;00m filename: tfp = [38;5;28mopen[39m(filename, [33m'[39m[33mwb[39m[33m'[39m)

[36mFile [39m[32m~/code/MasteringPyTorchV3/.venv/lib/python3.11/site-packages/fastcore/net.py:120[39m, in [36murlopen[39m[34m(url, data, headers, timeout, **kwargs)[39m
[32m    118[39m     [38;5;28;01mif[39;00m [38;5;129;01mnot[39;00m [38;5;28misinstance[39m(data, strtyps): data = urlencode(data)
[32m    119[39m     [38;5;28;01mif[39;00m [38;5;129;01mnot[39;00m [38;5;28misinstance[39m(data, [38;5;28mbytes[39m): data = data.encode([33m'[39m[33mascii[39m[33m'[39m)
[32m--> [39m[32m120[39m [38;5;28;01mtry[39;00m: [38;5;28;01mreturn[39;00m [30;43murlopener[39;49m[30;43m([39;49m[30;43m)[39;49m[30;43m.[39;49m[30;43mopen[39;49m[30;43m([39;49m[30;43murlwrap[39;49m[30;43m([39;49m[30;43murl[39;49m[30;43m,[39;49m[30;43m [39;49m[30;43mdata[39;49m[30;43m=[39;49m[30;43mdata[39;49m[30;43m,[39;49m[30;43m [39;49m[30;43mheaders[39;49m[30;43m=[39;49m[30;43mheaders[39;49m[30;43m)[39;49m[30;43m,[39;49m[30;43m [39;49m[30;43mtimeout[39;49m[30;43m=[39;49m[30;43mtimeout[39;49m[30;43m)[39;49m
[32m    121[39m [38;5;28;01mexcept[39;00m HTTPError [38;5;28;01mas[39;00m e: 
[32m    122[39m     e.msg += [33mf[39m[33m"[39m[38;5;130;01m\n[39;00m[33m====Error Body====[39m[38;5;130;01m\n[39;00m[38;5;132;01m{[39;00me.read().decode(errors=[33m'[39m[33mignore[39m[33m'[39m)[38;5;132;01m}[39;00m[33m"[39m

[36mFile [39m[32m/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/urllib/request.py:519[39m, in [36mOpenerDirector.open[39m[34m(self, fullurl, data, timeout)[39m
[32m    516[39m     req = meth(req)
[32m    518[39m sys.audit([33m'[39m[33murllib.Request[39m[33m'[39m, req.full_url, req.data, req.headers, req.get_method())
[32m--> [39m[32m519[39m response = [30;43mself[39;49m[30;43m.[39;49m[30;43m_open[39;49m[30;43m([39;49m[30;43mreq[39;49m[30;43m,[39;49m[30;43m [39;49m[30;43mdata[39;49m[30;43m)[39;49m
[32m    521[39m [38;5;66;03m# post-process response[39;00m
[32m    522[39m meth_name = protocol+[33m"[39m[33m_response[39m[33m"[39m

[36mFile [39m[32m/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/urllib/request.py:536[39m, in [36mOpenerDirector._open[39m[34m(self, req, data)[39m
[32m    533[39m     [38;5;28;01mreturn[39;00m result
[32m    535[39m protocol = req.type
[32m--> [39m[32m536[39m result = [30;43mself[39;49m[30;43m.[39;49m[30;43m_call_chain[39;49m[30;43m([39;49m[30;43mself[39;49m[30;43m.[39;49m[30;43mhandle_open[39;49m[30;43m,[39;49m[30;43m [39;49m[30;43mprotocol[39;49m[30;43m,[39;49m[30;43m [39;49m[30;43mprotocol[39;49m[30;43m [39;49m[30;43m+[39;49m
[32m    537[39m [30;43m                          [39;49m[30;43m'[39;49m[30;43m_open[39;49m[30;43m'[39;49m[30;43m,[39;49m[30;43m [39;49m[30;43mreq[39;49m[30;43m)[39;49m
[32m    538[39m [38;5;28;01mif[39;00m result:
[32m    539[39m     [38;5;28;01mreturn[39;00m result

[36mFile [39m[32m/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/urllib/request.py:496[39m, in [36mOpenerDirector._call_chain[39m[34m(self, chain, kind, meth_name, *args)[39m
[32m    494[39m [38;5;28;01mfor[39;00m handler [38;5;129;01min[39;00m handlers:
[32m    495[39m     func = [38;5;28mgetattr[39m(handler, meth_name)
[32m--> [39m[32m496[39m     result = [30;43mfunc[39;49m[30;43m([39;49m[30;43m*[39;49m[30;43margs[39;49m[30;43m)[39;49m
[32m    497[39m     [38;5;28;01mif[39;00m result [38;5;129;01mis[39;00m [38;5;129;01mnot[39;00m [38;5;28;01mNone[39;00m:
[32m    498[39m         [38;5;28;01mreturn[39;00m result

[36mFile [39m[32m/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/urllib/request.py:1391[39m, in [36mHTTPSHandler.https_open[39m[34m(self, req)[39m
[32m   1390[39m [38;5;28;01mdef[39;00m[38;5;250m [39m[34mhttps_open[39m([38;5;28mself[39m, req):
[32m-> [39m[32m1391[39m     [38;5;28;01mreturn[39;00m [30;43mself[39;49m[30;43m.[39;49m[30;43mdo_open[39;49m[30;43m([39;49m[30;43mhttp[39;49m[30;43m.[39;49m[30;43mclient[39;49m[30;43m.[39;49m[30;43mHTTPSConnection[39;49m[30;43m,[39;49m[30;43m [39;49m[30;43mreq[39;49m[30;43m,[39;49m
[32m   1392[39m [30;43m        [39;49m[30;43mcontext[39;49m[30;43m=[39;49m[30;43mself[39;49m[30;43m.[39;49m[30;43m_context[39;49m[30;43m,[39;49m[30;43m [39;49m[30;43mcheck_hostname[39;49m[30;43m=[39;49m[30;43mself[39;49m[30;43m.[39;49m[30;43m_check_hostname[39;49m[30;43m)[39;49m

[36mFile [39m[32m/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/urllib/request.py:1351[39m, in [36mAbstractHTTPHandler.do_open[39m[34m(self, http_class, req, **http_conn_args)[39m
[32m   1348[39m         h.request(req.get_method(), req.selector, req.data, headers,
[32m   1349[39m                   encode_chunked=req.has_header([33m'[39m[33mTransfer-encoding[39m[33m'[39m))
[32m   1350[39m     [38;5;28;01mexcept[39;00m [38;5;167;01mOSError[39;00m [38;5;28;01mas[39;00m err: [38;5;66;03m# timeout error[39;00m
[32m-> [39m[32m1351[39m         [38;5;28;01mraise[39;00m URLError(err)
[32m   1352[39m     r = h.getresponse()
[32m   1353[39m [38;5;28;01mexcept[39;00m:

[31mURLError[39m: <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1006)>


```

### `Chapter15/pytorch_lightning.ipynb`
```
Traceback (most recent call last):
  File "/Users/ashish/code/MasteringPyTorchV3/scripts/validate_notebooks.py", line 85, in run_one
    client.execute()
  File "/Users/ashish/code/MasteringPyTorchV3/.venv/lib/python3.11/site-packages/jupyter_core/utils/__init__.py", line 165, in wrapped
    return loop.run_until_complete(inner)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/asyncio/base_events.py", line 654, in run_until_complete
    return future.result()
           ^^^^^^^^^^^^^^^
  File "/Users/ashish/code/MasteringPyTorchV3/.venv/lib/python3.11/site-packages/nbclient/client.py", line 709, in async_execute
    await self.async_execute_cell(
  File "/Users/ashish/code/MasteringPyTorchV3/.venv/lib/python3.11/site-packages/nbclient/client.py", line 1062, in async_execute_cell
    await self._check_raise_for_error(cell, cell_index, exec_reply)
  File "/Users/ashish/code/MasteringPyTorchV3/.venv/lib/python3.11/site-packages/nbclient/client.py", line 918, in _check_raise_for_error
    raise CellExecutionError.from_cell_and_msg(cell, exec_reply_content)
nbclient.exceptions.CellExecutionError: An error occurred while executing the following cell:
------------------
model = ConvNet()

trainer = pl.Trainer(max_epochs=10)    
trainer.fit(model)   
------------------

----- stderr -----
GPU available: True (mps), used: True
----- stderr -----
TPU available: False, using: 0 TPU cores
----- stderr -----
/Users/ashish/code/MasteringPyTorchV3/.venv/lib/python3.11/site-packages/pytorch_lightning/trainer/connectors/logger_connector/logger_connector.py:76: Starting from v1.9.0, `tensorboardX` has been removed as a dependency of the `pytorch_lightning` package, due to potential conflicts with other packages in the ML ecosystem. For this reason, `logger=True` will use `CSVLogger` as the default logger, unless the `tensorboard` or `tensorboardX` packages are found. Please `pip install lightning[extra]` or one of them to enable TensorBoard support by default
💡 Tip: For seamless cloud logging and experiment tracking, try installing [litlogger](https://pypi.org/project/litlogger/) to enable LitLogger, which logs metrics and artifacts automatically to the Lightning Experiments platform.
----- stderr -----
💡 Tip: For seamless cloud uploads and versioning, try installing [litmodels](https://pypi.org/project/litmodels/) to enable LitModelCheckpoint, which syncs automatically with the Lightning model registry.
----- stderr -----
/Users/ashish/code/MasteringPyTorchV3/.venv/lib/python3.11/site-packages/pytorch_lightning/trainer/configuration_validator.py:68: You passed in a `val_dataloader` but have no `validation_step`. Skipping val loop.
------------------

[31m---------------------------------------------------------------------------[39m
[31mNotImplementedError[39m                       Traceback (most recent call last)
[36mCell[39m[36m [39m[32mIn[4][39m[32m, line 4[39m
[32m      1[39m model = ConvNet()
[32m      2[39m 
[32m      3[39m trainer = pl.Trainer(max_epochs=[32m10[39m)
[32m----> [39m[32m4[39m trainer.fit(model)

[36mFile [39m[32m~/code/MasteringPyTorchV3/.venv/lib/python3.11/site-packages/pytorch_lightning/trainer/trainer.py:584[39m, in [36mTrainer.fit[39m[34m(self, model, train_dataloaders, val_dataloaders, datamodule, ckpt_path, weights_only)[39m
[32m    582[39m [38;5;28mself[39m.training = [38;5;28;01mTrue[39;00m
[32m    583[39m [38;5;28mself[39m.should_stop = [38;5;28;01mFalse[39;00m
[32m--> [39m[32m584[39m [30;43mcall[39;49m[30;43m.[39;49m[30;43m_call_and_handle_interrupt[39;49m[30;43m([39;49m
[32m    585[39m [30;43m    [39;49m[30;43mself[39;49m[30;43m,[39;49m
[32m    586[39m [30;43m    [39;49m[30;43mself[39;49m[30;43m.[39;49m[30;43m_fit_impl[39;49m[30;43m,[39;49m
[32m    587[39m [30;43m    [39;49m[30;43mmodel[39;49m[30;43m,[39;49m
[32m    588[39m [30;43m    [39;49m[30;43mtrain_dataloaders[39;49m[30;43m,[39;49m
[32m    589[39m [30;43m    [39;49m[30;43mval_dataloaders[39;49m[30;43m,[39;49m
[32m    590[39m [30;43m    [39;49m[30;43mdatamodule[39;49m[30;43m,[39;49m
[32m    591[39m [30;43m    [39;49m[30;43mckpt_path[39;49m[30;43m,[39;49m
[32m    592[39m [30;43m    [39;49m[30;43mweights_only[39;49m[30;43m,[39;49m
[32m    593[39m [30;43m[39;49m[30;43m)[39;49m

[36mFile [39m[32m~/code/MasteringPyTorchV3/.venv/lib/python3.11/site-packages/pytorch_lightning/trainer/call.py:49[39m, in [36m_call_and_handle_interrupt[39m[34m(trainer, trainer_fn, *args, **kwargs)[39m
[32m     47[39m     [38;5;28;01mif[39;00m trainer.strategy.launcher [38;5;129;01mis[39;00m [38;5;129;01mnot[39;00m [38;5;28;01mNone[39;00m:
[32m     48[39m         [38;5;28;01mreturn[39;00m trainer.strategy.launcher.launch(trainer_fn, *args, trainer=trainer, **kwargs)
[32m---> [39m[32m49[39m     [38;5;28;01mreturn[39;00m [30;43mtrainer_fn[39;49m[30;43m([39;49m[30;43m*[39;49m[30;43margs[39;49m[30;43m,[39;49m[30;43m [39;49m[30;43m*[39;49m[30;43m*[39;49m[30;43mkwargs[39;49m[30;43m)[39;49m
[32m     51[39m [38;5;28;01mexcept[39;00m _TunerExitException:
[32m     52[39m     _call_teardown_hook(trainer)

[36mFile [39m[32m~/code/MasteringPyTorchV3/.venv/lib/python3.11/site-packages/pytorch_lightning/trainer/trainer.py:630[39m, in [36mTrainer._fit_impl[39m[34m(self, model, train_dataloaders, val_dataloaders, datamodule, ckpt_path, weights_only)[39m
[32m    623[39m     download_model_from_registry(ckpt_path, [38;5;28mself[39m)
[32m    624[39m ckpt_path = [38;5;28mself[39m._checkpoint_connector._select_ckpt_path(
[32m    625[39m     [38;5;28mself[39m.state.fn,
[32m    626[39m     ckpt_path,
[32m    627[39m     model_provided=[38;5;28;01mTrue[39;00m,
[32m    628[39m     model_connected=[38;5;28mself[39m.lightning_module [38;5;129;01mis[39;00m [38;5;129;01mnot[39;00m [38;5;28;01mNone[39;00m,
[32m    629[39m )
[32m--> [39m[32m630[39m [30;43mself[39;49m[30;43m.[39;49m[30;43m_run[39;49m[30;43m([39;49m[30;43mmodel[39;49m[30;43m,[39;49m[30;43m [39;49m[30;43mckpt_path[39;49m[30;43m=[39;49m[30;43mckpt_path[39;49m[30;43m,[39;49m[30;43m [39;49m[30;43mweights_only[39;49m[30;43m=[39;49m[30;43mweights_only[39;49m[30;43m)[39;49m
[32m    632[39m [38;5;28;01massert[39;00m [38;5;28mself[39m.state.stopped
[32m    633[39m [38;5;28mself[39m.training = [38;5;28;01mFalse[39;00m

[36mFile [39m[32m~/code/MasteringPyTorchV3/.venv/lib/python3.11/site-packages/pytorch_lightning/trainer/trainer.py:1027[39m, in [36mTrainer._run[39m[34m(self, model, ckpt_path, weights_only)[39m
[32m   1024[39m [38;5;28mself[39m._callback_connector._attach_model_callbacks()
[32m   1025[39m [38;5;28mself[39m._callback_connector._attach_model_logging_functions()
[32m-> [39m[32m1027[39m [30;43m_verify_loop_configurations[39;49m[30;43m([39;49m[30;43mself[39;49m[30;43m)[39;49m
[32m   1029[39m [38;5;66;03m# ----------------------------[39;00m
[32m   1030[39m [38;5;66;03m# SET UP THE TRAINER[39;00m
[32m   1031[39m [38;5;66;03m# ----------------------------[39;00m
[32m   1032[39m log.debug([33mf[39m[33m"[39m[38;5;132;01m{[39;00m[38;5;28mself[39m.[34m__class__[39m.[34m__name__[39m[38;5;132;01m}[39;00m[33m: setting up strategy environment[39m[33m"[39m)

[36mFile [39m[32m~/code/MasteringPyTorchV3/.venv/lib/python3.11/site-packages/pytorch_lightning/trainer/configuration_validator.py:36[39m, in [36m_verify_loop_configurations[39m[34m(trainer)[39m
[32m     34[39m     [38;5;28;01mraise[39;00m [38;5;167;01mValueError[39;00m([33m"[39m[33mUnexpected: Trainer state fn must be set before validating loop configuration.[39m[33m"[39m)
[32m     35[39m [38;5;28;01mif[39;00m trainer.state.fn == TrainerFn.FITTING:
[32m---> [39m[32m36[39m     [30;43m__verify_train_val_loop_configuration[39;49m[30;43m([39;49m[30;43mtrainer[39;49m[30;43m,[39;49m[30;43m [39;49m[30;43mmodel[39;49m[30;43m)[39;49m
[32m     37[39m     __verify_manual_optimization_support(trainer, model)
[32m     38[39m [38;5;28;01melif[39;00m trainer.state.fn == TrainerFn.VALIDATING:

[36mFile [39m[32m~/code/MasteringPyTorchV3/.venv/lib/python3.11/site-packages/pytorch_lightning/trainer/configuration_validator.py:84[39m, in [36m__verify_train_val_loop_configuration[39m[34m(trainer, model)[39m
[32m     77[39m     [38;5;28;01mraise[39;00m [38;5;167;01mNotImplementedError[39;00m(
[32m     78[39m         [33mf[39m[33m"[39m[33mSupport for `training_epoch_end` has been removed in v2.0.0. `[39m[38;5;132;01m{[39;00m[38;5;28mtype[39m(model).[34m__name__[39m[38;5;132;01m}[39;00m[33m` implements this[39m[33m"[39m
[32m     79[39m         [33m"[39m[33m method. You can use the `on_train_epoch_end` hook instead. To access outputs, save them in-memory as[39m[33m"[39m
[32m     80[39m         [33m"[39m[33m instance attributes.[39m[33m"[39m
[32m     81[39m         [33m"[39m[33m You can find migration examples in https://github.com/Lightning-AI/pytorch-lightning/pull/16520.[39m[33m"[39m
[32m     82[39m     )
[32m     83[39m [38;5;28;01mif[39;00m [38;5;28mcallable[39m([38;5;28mgetattr[39m(model, [33m"[39m[33mvalidation_epoch_end[39m[33m"[39m, [38;5;28;01mNone[39;00m)):
[32m---> [39m[32m84[39m     [38;5;28;01mraise[39;00m [38;5;167;01mNotImplementedError[39;00m(
[32m     85[39m         [33mf[39m[33m"[39m[33mSupport for `validation_epoch_end` has been removed in v2.0.0. `[39m[38;5;132;01m{[39;00m[38;5;28mtype[39m(model).[34m__name__[39m[38;5;132;01m}[39;00m[33m` implements this[39m[33m"[39m
[32m     86[39m         [33m"[39m[33m method. You can use the `on_validation_epoch_end` hook instead. To access outputs, save them in-memory as[39m[33m"[39m
[32m     87[39m         [33m"[39m[33m instance attributes.[39m[33m"[39m
[32m     88[39m         [33m"[39m[33m You can find migration examples in https://github.com/Lightning-AI/pytorch-lightning/pull/16520.[39m[33m"[39m
[32m     89[39m     )

[31mNotImplementedError[39m: Support for `validation_epoch_end` has been removed in v2.0.0. `ConvNet` implements this method. You can use the `on_validation_epoch_end` hook instead. To access outputs, save them in-memory as instance attributes. You can find migration examples in https://github.com/Lightning-AI/pytorch-lightning/pull/16520.


```

### `Chapter15/pytorch_profiler.ipynb`
```
Traceback (most recent call last):
  File "/Users/ashish/code/MasteringPyTorchV3/scripts/validate_notebooks.py", line 85, in run_one
    client.execute()
  File "/Users/ashish/code/MasteringPyTorchV3/.venv/lib/python3.11/site-packages/jupyter_core/utils/__init__.py", line 165, in wrapped
    return loop.run_until_complete(inner)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/asyncio/base_events.py", line 654, in run_until_complete
    return future.result()
           ^^^^^^^^^^^^^^^
  File "/Users/ashish/code/MasteringPyTorchV3/.venv/lib/python3.11/site-packages/nbclient/client.py", line 709, in async_execute
    await self.async_execute_cell(
  File "/Users/ashish/code/MasteringPyTorchV3/.venv/lib/python3.11/site-packages/nbclient/client.py", line 1062, in async_execute_cell
    await self._check_raise_for_error(cell, cell_index, exec_reply)
  File "/Users/ashish/code/MasteringPyTorchV3/.venv/lib/python3.11/site-packages/nbclient/client.py", line 918, in _check_raise_for_error
    raise CellExecutionError.from_cell_and_msg(cell, exec_reply_content)
nbclient.exceptions.CellExecutionError: An error occurred while executing the following cell:
------------------
# The mean and standard deviation values are calculated as the mean of all pixel values of all images in the training dataset
train_dataloader = torch.utils.data.DataLoader(
    datasets.MNIST('../data', train=True, download=True,
                   transform=transforms.Compose([
                       transforms.ToTensor(),
                       transforms.Normalize((0.1302,), (0.3069,))])), # train_X.mean()/256. and train_X.std()/256.
    batch_size=32, shuffle=True)

test_dataloader = torch.utils.data.DataLoader(
    datasets.MNIST('../data', train=False, 
                   transform=transforms.Compose([
                       transforms.ToTensor(),
                       transforms.Normalize((0.1302,), (0.3069,)) 
                   ])),
    batch_size=500, shuffle=False)
------------------


[31m---------------------------------------------------------------------------[39m
[31mRuntimeError[39m                              Traceback (most recent call last)
[36mCell[39m[36m [39m[32mIn[6][39m[32m, line 3[39m
[32m      1[39m [38;5;66;03m# The mean and standard deviation values are calculated as the mean of all pixel values of all images in the training dataset[39;00m
[32m      2[39m train_dataloader = torch.utils.data.DataLoader(
[32m----> [39m[32m3[39m     datasets.MNIST('../data', train=True, download=True,
[32m      4[39m                    transform=transforms.Compose([
[32m      5[39m                        transforms.ToTensor(),
[32m      6[39m                        transforms.Normalize((0.1302,), (0.3069,))])), # train_X.mean()/256. and train_X.std()/256.

[36mFile [39m[32m~/code/MasteringPyTorchV3/.venv/lib/python3.11/site-packages/torchvision/datasets/mnist.py:100[39m, in [36mMNIST.__init__[39m[34m(self, root, train, transform, target_transform, download)[39m
[32m     97[39m     [38;5;28;01mreturn[39;00m
[32m     99[39m [38;5;28;01mif[39;00m download:
[32m--> [39m[32m100[39m     [30;43mself[39;49m[30;43m.[39;49m[30;43mdownload[39;49m[30;43m([39;49m[30;43m)[39;49m
[32m    102[39m [38;5;28;01mif[39;00m [38;5;129;01mnot[39;00m [38;5;28mself[39m._check_exists():
[32m    103[39m     [38;5;28;01mraise[39;00m [38;5;167;01mRuntimeError[39;00m([33m"[39m[33mDataset not found. You can use download=True to download it[39m[33m"[39m)

[36mFile [39m[32m~/code/MasteringPyTorchV3/.venv/lib/python3.11/site-packages/torchvision/datasets/mnist.py:197[39m, in [36mMNIST.download[39m[34m(self)[39m
[32m    195[39m [38;5;28;01mfor[39;00m mirror, err [38;5;129;01min[39;00m [38;5;28mzip[39m([38;5;28mself[39m.mirrors, errors):
[32m    196[39m     s += [33mf[39m[33m"[39m[33mTried [39m[38;5;132;01m{[39;00mmirror[38;5;132;01m}[39;00m[33m, got:[39m[38;5;130;01m\n[39;00m[38;5;132;01m{[39;00m[38;5;28mstr[39m(err)[38;5;132;01m}[39;00m[38;5;130;01m\n[39;00m[33m"[39m
[32m--> [39m[32m197[39m [38;5;28;01mraise[39;00m [38;5;167;01mRuntimeError[39;00m(s)

[31mRuntimeError[39m: Error downloading train-images-idx3-ubyte.gz:
Tried https://ossci-datasets.s3.amazonaws.com/mnist/, got:
<urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1006)>
Tried http://yann.lecun.com/exdb/mnist/, got:
HTTP Error 404: Not Found



```

### `Chapter17/captum_interpretability.ipynb`
```
Traceback (most recent call last):
  File "/Users/ashish/code/MasteringPyTorchV3/scripts/validate_notebooks.py", line 85, in run_one
    client.execute()
  File "/Users/ashish/code/MasteringPyTorchV3/.venv/lib/python3.11/site-packages/jupyter_core/utils/__init__.py", line 165, in wrapped
    return loop.run_until_complete(inner)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/asyncio/base_events.py", line 654, in run_until_complete
    return future.result()
           ^^^^^^^^^^^^^^^
  File "/Users/ashish/code/MasteringPyTorchV3/.venv/lib/python3.11/site-packages/nbclient/client.py", line 709, in async_execute
    await self.async_execute_cell(
  File "/Users/ashish/code/MasteringPyTorchV3/.venv/lib/python3.11/site-packages/nbclient/client.py", line 1062, in async_execute_cell
    await self._check_raise_for_error(cell, cell_index, exec_reply)
  File "/Users/ashish/code/MasteringPyTorchV3/.venv/lib/python3.11/site-packages/nbclient/client.py", line 918, in _check_raise_for_error
    raise CellExecutionError.from_cell_and_msg(cell, exec_reply_content)
nbclient.exceptions.CellExecutionError: An error occurred while executing the following cell:
------------------
# The mean and standard deviation values are calculated as the mean of all pixel values of all images in the training dataset
train_dataloader = torch.utils.data.DataLoader(
    datasets.MNIST('../data', train=True, download=True,
                   transform=transforms.Compose([
                       transforms.ToTensor(),
                       transforms.Normalize((0.1302,), (0.3069,))])), # train_X.mean()/256. and train_X.std()/256.
    batch_size=32, shuffle=True)

test_dataloader = torch.utils.data.DataLoader(
    datasets.MNIST('../data', train=False, 
                   transform=transforms.Compose([
                       transforms.ToTensor(),
                       transforms.Normalize((0.1302,), (0.3069,)) 
                   ])),
    batch_size=500, shuffle=True)
------------------


[31m---------------------------------------------------------------------------[39m
[31mRuntimeError[39m                              Traceback (most recent call last)
[36mCell[39m[36m [39m[32mIn[7][39m[32m, line 3[39m
[32m      1[39m [38;5;66;03m# The mean and standard deviation values are calculated as the mean of all pixel values of all images in the training dataset[39;00m
[32m      2[39m train_dataloader = torch.utils.data.DataLoader(
[32m----> [39m[32m3[39m     datasets.MNIST('../data', train=True, download=True,
[32m      4[39m                    transform=transforms.Compose([
[32m      5[39m                        transforms.ToTensor(),
[32m      6[39m                        transforms.Normalize((0.1302,), (0.3069,))])), # train_X.mean()/256. and train_X.std()/256.

[36mFile [39m[32m~/code/MasteringPyTorchV3/.venv/lib/python3.11/site-packages/torchvision/datasets/mnist.py:100[39m, in [36mMNIST.__init__[39m[34m(self, root, train, transform, target_transform, download)[39m
[32m     97[39m     [38;5;28;01mreturn[39;00m
[32m     99[39m [38;5;28;01mif[39;00m download:
[32m--> [39m[32m100[39m     [30;43mself[39;49m[30;43m.[39;49m[30;43mdownload[39;49m[30;43m([39;49m[30;43m)[39;49m
[32m    102[39m [38;5;28;01mif[39;00m [38;5;129;01mnot[39;00m [38;5;28mself[39m._check_exists():
[32m    103[39m     [38;5;28;01mraise[39;00m [38;5;167;01mRuntimeError[39;00m([33m"[39m[33mDataset not found. You can use download=True to download it[39m[33m"[39m)

[36mFile [39m[32m~/code/MasteringPyTorchV3/.venv/lib/python3.11/site-packages/torchvision/datasets/mnist.py:197[39m, in [36mMNIST.download[39m[34m(self)[39m
[32m    195[39m [38;5;28;01mfor[39;00m mirror, err [38;5;129;01min[39;00m [38;5;28mzip[39m([38;5;28mself[39m.mirrors, errors):
[32m    196[39m     s += [33mf[39m[33m"[39m[33mTried [39m[38;5;132;01m{[39;00mmirror[38;5;132;01m}[39;00m[33m, got:[39m[38;5;130;01m\n[39;00m[38;5;132;01m{[39;00m[38;5;28mstr[39m(err)[38;5;132;01m}[39;00m[38;5;130;01m\n[39;00m[33m"[39m
[32m--> [39m[32m197[39m [38;5;28;01mraise[39;00m [38;5;167;01mRuntimeError[39;00m(s)

[31mRuntimeError[39m: Error downloading train-images-idx3-ubyte.gz:
Tried https://ossci-datasets.s3.amazonaws.com/mnist/, got:
<urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1006)>
Tried http://yann.lecun.com/exdb/mnist/, got:
HTTP Error 404: Not Found



```

### `Chapter17/pytorch_interpretability.ipynb`
```
Traceback (most recent call last):
  File "/Users/ashish/code/MasteringPyTorchV3/scripts/validate_notebooks.py", line 85, in run_one
    client.execute()
  File "/Users/ashish/code/MasteringPyTorchV3/.venv/lib/python3.11/site-packages/jupyter_core/utils/__init__.py", line 165, in wrapped
    return loop.run_until_complete(inner)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/asyncio/base_events.py", line 654, in run_until_complete
    return future.result()
           ^^^^^^^^^^^^^^^
  File "/Users/ashish/code/MasteringPyTorchV3/.venv/lib/python3.11/site-packages/nbclient/client.py", line 709, in async_execute
    await self.async_execute_cell(
  File "/Users/ashish/code/MasteringPyTorchV3/.venv/lib/python3.11/site-packages/nbclient/client.py", line 1062, in async_execute_cell
    await self._check_raise_for_error(cell, cell_index, exec_reply)
  File "/Users/ashish/code/MasteringPyTorchV3/.venv/lib/python3.11/site-packages/nbclient/client.py", line 918, in _check_raise_for_error
    raise CellExecutionError.from_cell_and_msg(cell, exec_reply_content)
nbclient.exceptions.CellExecutionError: An error occurred while executing the following cell:
------------------
# The mean and standard deviation values are calculated as the mean of all pixel values of all images in the training dataset
train_dataloader = torch.utils.data.DataLoader(
    datasets.MNIST('../data', train=True, download=True,
                   transform=transforms.Compose([
                       transforms.ToTensor(),
                       transforms.Normalize((0.1302,), (0.3069,))])), # train_X.mean()/256. and train_X.std()/256.
    batch_size=32, shuffle=True)

test_dataloader = torch.utils.data.DataLoader(
    datasets.MNIST('../data', train=False, 
                   transform=transforms.Compose([
                       transforms.ToTensor(),
                       transforms.Normalize((0.1302,), (0.3069,)) 
                   ])),
    batch_size=500, shuffle=True)
------------------


[31m---------------------------------------------------------------------------[39m
[31mRuntimeError[39m                              Traceback (most recent call last)
[36mCell[39m[36m [39m[32mIn[7][39m[32m, line 3[39m
[32m      1[39m [38;5;66;03m# The mean and standard deviation values are calculated as the mean of all pixel values of all images in the training dataset[39;00m
[32m      2[39m train_dataloader = torch.utils.data.DataLoader(
[32m----> [39m[32m3[39m     datasets.MNIST('../data', train=True, download=True,
[32m      4[39m                    transform=transforms.Compose([
[32m      5[39m                        transforms.ToTensor(),
[32m      6[39m                        transforms.Normalize((0.1302,), (0.3069,))])), # train_X.mean()/256. and train_X.std()/256.

[36mFile [39m[32m~/code/MasteringPyTorchV3/.venv/lib/python3.11/site-packages/torchvision/datasets/mnist.py:100[39m, in [36mMNIST.__init__[39m[34m(self, root, train, transform, target_transform, download)[39m
[32m     97[39m     [38;5;28;01mreturn[39;00m
[32m     99[39m [38;5;28;01mif[39;00m download:
[32m--> [39m[32m100[39m     [30;43mself[39;49m[30;43m.[39;49m[30;43mdownload[39;49m[30;43m([39;49m[30;43m)[39;49m
[32m    102[39m [38;5;28;01mif[39;00m [38;5;129;01mnot[39;00m [38;5;28mself[39m._check_exists():
[32m    103[39m     [38;5;28;01mraise[39;00m [38;5;167;01mRuntimeError[39;00m([33m"[39m[33mDataset not found. You can use download=True to download it[39m[33m"[39m)

[36mFile [39m[32m~/code/MasteringPyTorchV3/.venv/lib/python3.11/site-packages/torchvision/datasets/mnist.py:197[39m, in [36mMNIST.download[39m[34m(self)[39m
[32m    195[39m [38;5;28;01mfor[39;00m mirror, err [38;5;129;01min[39;00m [38;5;28mzip[39m([38;5;28mself[39m.mirrors, errors):
[32m    196[39m     s += [33mf[39m[33m"[39m[33mTried [39m[38;5;132;01m{[39;00mmirror[38;5;132;01m}[39;00m[33m, got:[39m[38;5;130;01m\n[39;00m[38;5;132;01m{[39;00m[38;5;28mstr[39m(err)[38;5;132;01m}[39;00m[38;5;130;01m\n[39;00m[33m"[39m
[32m--> [39m[32m197[39m [38;5;28;01mraise[39;00m [38;5;167;01mRuntimeError[39;00m(s)

[31mRuntimeError[39m: Error downloading train-images-idx3-ubyte.gz:
Tried https://ossci-datasets.s3.amazonaws.com/mnist/, got:
<urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1006)>
Tried http://yann.lecun.com/exdb/mnist/, got:
HTTP Error 404: Not Found



```

