# Notebook validation report

**When:** 2026-08-03 01:23 UTC
**Scope:** Wave 1
**Result:** 4 passed, 11 failed, 15 total

| Notebook | Status | Seconds | Error |
|---|---|---:|---|
| `Chapter01/mnist_pytorch.ipynb` | fail | 43.42 | CellExecutionError: An error occurred while executing the following cell: ------------------ for epoch in range(1, 3):     train(model, device, train_dataloader, optimizer, epoch)  |
| `Chapter01/pytorch2x_compile_demo.ipynb` | fail | 3.13 | CellExecutionError: An error occurred while executing the following cell: ------------------ tfm = transforms.Compose([     transforms.ToTensor(),     transforms.Normalize((0.1307, |
| `Chapter02/lenet.ipynb` | fail | 605.3 | CellTimeoutError: A cell timed out while it was being executed, after 600 seconds. The message was: Cell execution timed out. Here is a preview of the cell contents: -------------- |
| `Chapter02/transfer_learning_alexnet.ipynb` | fail | 5.32 | CellExecutionError: An error occurred while executing the following cell: ------------------ def imageshow(img, text=None):     img = img.numpy().transpose((1, 2, 0))     avg = np. |
| `Chapter02/vgg13_pretrained_run_inference.ipynb` | fail | 8.9 | CellExecutionError: An error occurred while executing the following cell: ------------------ visualize_predictions(model) ------------------  ----- stderr -----  A module that was  |
| `Chapter02/ResNetBlock.ipynb` | pass | 2.64 |  |
| `Chapter02/DenseNetBlock.ipynb` | pass | 1.18 |  |
| `Chapter02/GoogLeNet.ipynb` | pass | 2.48 |  |
| `Chapter03/rnn.ipynb` | fail | 1.8 | CellExecutionError: An error occurred while executing the following cell: ------------------ # read sentiments and reviews data from the text files review_list = [] label_list = [] |
| `Chapter03/lstm.ipynb` | fail | 9.81 | CellExecutionError: An error occurred while executing the following cell: ------------------ import random from torchtext.legacy import datasets from torchtext.legacy import data - |
| `Chapter15/fastai.ipynb` | pass | 336.04 |  |
| `Chapter15/pytorch_lightning.ipynb` | fail | 185.71 | AssertionError:  |
| `Chapter15/pytorch_profiler.ipynb` | fail | 4.09 | AssertionError:  |
| `Chapter17/captum_interpretability.ipynb` | fail | 3.72 | AssertionError:  |
| `Chapter17/pytorch_interpretability.ipynb` | fail | 4.54 | AssertionError:  |

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
for epoch in range(1, 3):
    train(model, device, train_dataloader, optimizer, epoch)
    test(model, device, test_dataloader)
------------------


[31m---------------------------------------------------------------------------[39m
[31mRuntimeError[39m                              Traceback (most recent call last)
[36mCell[39m[36m [39m[32mIn[8][39m[32m, line 2[39m
[32m      1[39m [38;5;28;01mfor[39;00m epoch [38;5;28;01min[39;00m range([32m1[39m, [32m3[39m):
[32m----> [39m[32m2[39m     train(model, device, train_dataloader, optimizer, epoch)
[32m      3[39m     test(model, device, test_dataloader)

[36mCell[39m[36m [39m[32mIn[4][39m[32m, line 3[39m, in [36mtrain[39m[34m(model, device, train_dataloader, optim, epoch)[39m
[32m      1[39m [38;5;28;01mdef[39;00m train(model, device, train_dataloader, optim, epoch):
[32m      2[39m     model.train()
[32m----> [39m[32m3[39m     [38;5;28;01mfor[39;00m b_i, (X, y) [38;5;28;01min[39;00m enumerate(train_dataloader):
[32m      4[39m         X, y = X.to(device), y.to(device)
[32m      5[39m         optim.zero_grad()
[32m      6[39m         pred_prob = model(X)

[36mFile [39m[32m~/code/MasteringPyTorchV3/.venv/lib/python3.11/site-packages/torch/utils/data/dataloader.py:631[39m, in [36m_BaseDataLoaderIter.__next__[39m[34m(self)[39m
[32m    628[39m [38;5;28;01mif[39;00m [38;5;28mself[39m._sampler_iter [38;5;129;01mis[39;00m [38;5;28;01mNone[39;00m:
[32m    629[39m     [38;5;66;03m# TODO(https://github.com/pytorch/pytorch/issues/76750)[39;00m
[32m    630[39m     [38;5;28mself[39m._reset()  [38;5;66;03m# type: ignore[call-arg][39;00m
[32m--> [39m[32m631[39m data = [30;43mself[39;49m[30;43m.[39;49m[30;43m_next_data[39;49m[30;43m([39;49m[30;43m)[39;49m
[32m    632[39m [38;5;28mself[39m._num_yielded += [32m1[39m
[32m    633[39m [38;5;28;01mif[39;00m [38;5;28mself[39m._dataset_kind == _DatasetKind.Iterable [38;5;129;01mand[39;00m \
[32m    634[39m         [38;5;28mself[39m._IterableDataset_len_called [38;5;129;01mis[39;00m [38;5;129;01mnot[39;00m [38;5;28;01mNone[39;00m [38;5;129;01mand[39;00m \
[32m    635[39m         [38;5;28mself[39m._num_yielded > [38;5;28mself[39m._IterableDataset_len_called:

[36mFile [39m[32m~/code/MasteringPyTorchV3/.venv/lib/python3.11/site-packages/torch/utils/data/dataloader.py:675[39m, in [36m_SingleProcessDataLoaderIter._next_data[39m[34m(self)[39m
[32m    673[39m [38;5;28;01mdef[39;00m[38;5;250m [39m[34m_next_data[39m([38;5;28mself[39m):
[32m    674[39m     index = [38;5;28mself[39m._next_index()  [38;5;66;03m# may raise StopIteration[39;00m
[32m--> [39m[32m675[39m     data = [30;43mself[39;49m[30;43m.[39;49m[30;43m_dataset_fetcher[39;49m[30;43m.[39;49m[30;43mfetch[39;49m[30;43m([39;49m[30;43mindex[39;49m[30;43m)[39;49m  [38;5;66;03m# may raise StopIteration[39;00m
[32m    676[39m     [38;5;28;01mif[39;00m [38;5;28mself[39m._pin_memory:
[32m    677[39m         data = _utils.pin_memory.pin_memory(data, [38;5;28mself[39m._pin_memory_device)

[36mFile [39m[32m~/code/MasteringPyTorchV3/.venv/lib/python3.11/site-packages/torch/utils/data/_utils/fetch.py:51[39m, in [36m_MapDatasetFetcher.fetch[39m[34m(self, possibly_batched_index)[39m
[32m     49[39m         data = [38;5;28mself[39m.dataset.__getitems__(possibly_batched_index)
[32m     50[39m     [38;5;28;01melse[39;00m:
[32m---> [39m[32m51[39m         data = [30;43m[[39;49m[30;43mself[39;49m[30;43m.[39;49m[30;43mdataset[39;49m[30;43m[[39;49m[30;43midx[39;49m[30;43m][39;49m[30;43m [39;49m[30;43;01mfor[39;49;00m[30;43m [39;49m[30;43midx[39;49m[30;43m [39;49m[30;43;01min[39;49;00m[30;43m [39;49m[30;43mpossibly_batched_index[39;49m[30;43m][39;49m
[32m     52[39m [38;5;28;01melse[39;00m:
[32m     53[39m     data = [38;5;28mself[39m.dataset[possibly_batched_index]

[36mFile [39m[32m~/code/MasteringPyTorchV3/.venv/lib/python3.11/site-packages/torch/utils/data/_utils/fetch.py:51[39m, in [36m<listcomp>[39m[34m(.0)[39m
[32m     49[39m         data = [38;5;28mself[39m.dataset.__getitems__(possibly_batched_index)
[32m     50[39m     [38;5;28;01melse[39;00m:
[32m---> [39m[32m51[39m         data = [[30;43mself[39;49m[30;43m.[39;49m[30;43mdataset[39;49m[30;43m[[39;49m[30;43midx[39;49m[30;43m][39;49m [38;5;28;01mfor[39;00m idx [38;5;129;01min[39;00m possibly_batched_index]
[32m     52[39m [38;5;28;01melse[39;00m:
[32m     53[39m     data = [38;5;28mself[39m.dataset[possibly_batched_index]

[36mFile [39m[32m~/code/MasteringPyTorchV3/.venv/lib/python3.11/site-packages/torchvision/datasets/mnist.py:142[39m, in [36mMNIST.__getitem__[39m[34m(self, index)[39m
[32m    138[39m img, target = [38;5;28mself[39m.data[index], [38;5;28mint[39m([38;5;28mself[39m.targets[index])
[32m    140[39m [38;5;66;03m# doing this so that it is consistent with all other datasets[39;00m
[32m    141[39m [38;5;66;03m# to return a PIL Image[39;00m
[32m--> [39m[32m142[39m img = Image.fromarray([30;43mimg[39;49m[30;43m.[39;49m[30;43mnumpy[39;49m[30;43m([39;49m[30;43m)[39;49m, mode=[33m"[39m[33mL[39m[33m"[39m)
[32m    144[39m [38;5;28;01mif[39;00m [38;5;28mself[39m.transform [38;5;129;01mis[39;00m [38;5;129;01mnot[39;00m [38;5;28;01mNone[39;00m:
[32m    145[39m     img = [38;5;28mself[39m.transform(img)

[31mRuntimeError[39m: Numpy is not available


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
[36mCell[39m[36m [39m[32mIn[3][39m[32m, line 6[39m
[32m      2[39m     transforms.ToTensor(),
[32m      3[39m     transforms.Normalize(([32m0.1307[39m,), ([32m0.3081[39m,)),
[32m      4[39m ])
[32m      5[39m ds = datasets.MNIST(root=[33m"./data"[39m, train=[38;5;28;01mFalse[39;00m, download=[38;5;28;01mTrue[39;00m, transform=tfm)
[32m----> [39m[32m6[39m x = torch.stack([ds[i][[32m0[39m] [38;5;28;01mfor[39;00m i [38;5;28;01min[39;00m range([32m64[39m)]).to(device)
[32m      7[39m 
[32m      8[39m @torch.inference_mode()
[32m      9[39m [38;5;28;01mdef[39;00m bench(fn, warmup=[32m5[39m, iters=[32m50[39m):

[36mCell[39m[36m [39m[32mIn[3][39m[32m, line 6[39m, in [36m<listcomp>[39m[34m(.0)[39m
[32m----> [39m[32m6[39m tfm = transforms.Compose([
[32m      7[39m     transforms.ToTensor(),
[32m      8[39m     transforms.Normalize(([32m0.1307[39m,), ([32m0.3081[39m,)),
[32m      9[39m ])

[36mFile [39m[32m~/code/MasteringPyTorchV3/.venv/lib/python3.11/site-packages/torchvision/datasets/mnist.py:142[39m, in [36mMNIST.__getitem__[39m[34m(self, index)[39m
[32m    138[39m img, target = [38;5;28mself[39m.data[index], [38;5;28mint[39m([38;5;28mself[39m.targets[index])
[32m    140[39m [38;5;66;03m# doing this so that it is consistent with all other datasets[39;00m
[32m    141[39m [38;5;66;03m# to return a PIL Image[39;00m
[32m--> [39m[32m142[39m img = Image.fromarray([30;43mimg[39;49m[30;43m.[39;49m[30;43mnumpy[39;49m[30;43m([39;49m[30;43m)[39;49m, mode=[33m"[39m[33mL[39m[33m"[39m)
[32m    144[39m [38;5;28;01mif[39;00m [38;5;28mself[39m.transform [38;5;129;01mis[39;00m [38;5;129;01mnot[39;00m [38;5;28;01mNone[39;00m:
[32m    145[39m     img = [38;5;28mself[39m.transform(img)

[31mRuntimeError[39m: Numpy is not available


```

### `Chapter02/lenet.ipynb`
```
Traceback (most recent call last):
  File "/Users/ashish/code/MasteringPyTorchV3/.venv/lib/python3.11/site-packages/nbclient/client.py", line 782, in _async_poll_for_reply
    msg = await ensure_async(self.kc.shell_channel.get_msg(timeout=new_timeout))
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/ashish/code/MasteringPyTorchV3/.venv/lib/python3.11/site-packages/jupyter_core/utils/__init__.py", line 214, in ensure_async
    result = await obj
             ^^^^^^^^^
  File "/Users/ashish/code/MasteringPyTorchV3/.venv/lib/python3.11/site-packages/jupyter_client/channels.py", line 330, in get_msg
    raise Empty
_queue.Empty

During handling of the above exception, another exception occurred:

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
  File "/Users/ashish/code/MasteringPyTorchV3/.venv/lib/python3.11/site-packages/nbclient/client.py", line 1005, in async_execute_cell
    exec_reply = await self.task_poll_for_reply
                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/ashish/code/MasteringPyTorchV3/.venv/lib/python3.11/site-packages/nbclient/client.py", line 806, in _async_poll_for_reply
    error_on_timeout_execute_reply = await self._async_handle_timeout(timeout, cell)
                                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/ashish/code/MasteringPyTorchV3/.venv/lib/python3.11/site-packages/nbclient/client.py", line 856, in _async_handle_timeout
    raise CellTimeoutError.error_from_timeout_and_cell(
nbclient.exceptions.CellTimeoutError: A cell timed out while it was being executed, after 600 seconds.
The message was: Cell execution timed out.
Here is a preview of the cell contents:
-------------------
['# The mean and std are kept as 0.5 for normalizing pixel values as the pixel values are originally in the range 0 to 1', 'train_transform = transforms.Compose([transforms.RandomHorizontalFlip(),', '                                      transforms.RandomCrop(32, 4),', '                                      transforms.ToTensor(),', '                                      transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))])']
...
['testloader = torch.utils.data.DataLoader(testset, batch_size=10000, shuffle=False)', '', '', '# ordering is important', "classes = ('plane', 'car', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck')"]
-------------------


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
def imageshow(img, text=None):
    img = img.numpy().transpose((1, 2, 0))
    avg = np.array([0.490, 0.449, 0.411])
    stddev = np.array([0.231, 0.221, 0.230])
    img = stddev * img + avg
    img = np.clip(img, 0, 1)
    plt.imshow(img)
    if text is not None:
        plt.title(text)

# Generate one train dataset batch
imgs, cls = next(iter(dloaders['train']))

# Generate a grid from batch
grid = torchvision.utils.make_grid(imgs)

imageshow(grid, text=[classes[c] for c in cls])
------------------


[31m---------------------------------------------------------------------------[39m
[31mRuntimeError[39m                              Traceback (most recent call last)
[36mCell[39m[36m [39m[32mIn[4][39m[32m, line 12[39m
[32m      8[39m     [38;5;28;01mif[39;00m text [38;5;28;01mis[39;00m [38;5;28;01mnot[39;00m [38;5;28;01mNone[39;00m:
[32m      9[39m         plt.title(text)
[32m     10[39m 
[32m     11[39m [38;5;66;03m# Generate one train dataset batch[39;00m
[32m---> [39m[32m12[39m imgs, cls = next(iter(dloaders[[33m'train'[39m]))
[32m     13[39m 
[32m     14[39m [38;5;66;03m# Generate a grid from batch[39;00m
[32m     15[39m grid = torchvision.utils.make_grid(imgs)

[36mFile [39m[32m~/code/MasteringPyTorchV3/.venv/lib/python3.11/site-packages/torch/utils/data/dataloader.py:631[39m, in [36m_BaseDataLoaderIter.__next__[39m[34m(self)[39m
[32m    628[39m [38;5;28;01mif[39;00m [38;5;28mself[39m._sampler_iter [38;5;129;01mis[39;00m [38;5;28;01mNone[39;00m:
[32m    629[39m     [38;5;66;03m# TODO(https://github.com/pytorch/pytorch/issues/76750)[39;00m
[32m    630[39m     [38;5;28mself[39m._reset()  [38;5;66;03m# type: ignore[call-arg][39;00m
[32m--> [39m[32m631[39m data = [30;43mself[39;49m[30;43m.[39;49m[30;43m_next_data[39;49m[30;43m([39;49m[30;43m)[39;49m
[32m    632[39m [38;5;28mself[39m._num_yielded += [32m1[39m
[32m    633[39m [38;5;28;01mif[39;00m [38;5;28mself[39m._dataset_kind == _DatasetKind.Iterable [38;5;129;01mand[39;00m \
[32m    634[39m         [38;5;28mself[39m._IterableDataset_len_called [38;5;129;01mis[39;00m [38;5;129;01mnot[39;00m [38;5;28;01mNone[39;00m [38;5;129;01mand[39;00m \
[32m    635[39m         [38;5;28mself[39m._num_yielded > [38;5;28mself[39m._IterableDataset_len_called:

[36mFile [39m[32m~/code/MasteringPyTorchV3/.venv/lib/python3.11/site-packages/torch/utils/data/dataloader.py:675[39m, in [36m_SingleProcessDataLoaderIter._next_data[39m[34m(self)[39m
[32m    673[39m [38;5;28;01mdef[39;00m[38;5;250m [39m[34m_next_data[39m([38;5;28mself[39m):
[32m    674[39m     index = [38;5;28mself[39m._next_index()  [38;5;66;03m# may raise StopIteration[39;00m
[32m--> [39m[32m675[39m     data = [30;43mself[39;49m[30;43m.[39;49m[30;43m_dataset_fetcher[39;49m[30;43m.[39;49m[30;43mfetch[39;49m[30;43m([39;49m[30;43mindex[39;49m[30;43m)[39;49m  [38;5;66;03m# may raise StopIteration[39;00m
[32m    676[39m     [38;5;28;01mif[39;00m [38;5;28mself[39m._pin_memory:
[32m    677[39m         data = _utils.pin_memory.pin_memory(data, [38;5;28mself[39m._pin_memory_device)

[36mFile [39m[32m~/code/MasteringPyTorchV3/.venv/lib/python3.11/site-packages/torch/utils/data/_utils/fetch.py:51[39m, in [36m_MapDatasetFetcher.fetch[39m[34m(self, possibly_batched_index)[39m
[32m     49[39m         data = [38;5;28mself[39m.dataset.__getitems__(possibly_batched_index)
[32m     50[39m     [38;5;28;01melse[39;00m:
[32m---> [39m[32m51[39m         data = [30;43m[[39;49m[30;43mself[39;49m[30;43m.[39;49m[30;43mdataset[39;49m[30;43m[[39;49m[30;43midx[39;49m[30;43m][39;49m[30;43m [39;49m[30;43;01mfor[39;49;00m[30;43m [39;49m[30;43midx[39;49m[30;43m [39;49m[30;43;01min[39;49;00m[30;43m [39;49m[30;43mpossibly_batched_index[39;49m[30;43m][39;49m
[32m     52[39m [38;5;28;01melse[39;00m:
[32m     53[39m     data = [38;5;28mself[39m.dataset[possibly_batched_index]

[36mFile [39m[32m~/code/MasteringPyTorchV3/.venv/lib/python3.11/site-packages/torch/utils/data/_utils/fetch.py:51[39m, in [36m<listcomp>[39m[34m(.0)[39m
[32m     49[39m         data = [38;5;28mself[39m.dataset.__getitems__(possibly_batched_index)
[32m     50[39m     [38;5;28;01melse[39;00m:
[32m---> [39m[32m51[39m         data = [[30;43mself[39;49m[30;43m.[39;49m[30;43mdataset[39;49m[30;43m[[39;49m[30;43midx[39;49m[30;43m][39;49m [38;5;28;01mfor[39;00m idx [38;5;129;01min[39;00m possibly_batched_index]
[32m     52[39m [38;5;28;01melse[39;00m:
[32m     53[39m     data = [38;5;28mself[39m.dataset[possibly_batched_index]

[36mFile [39m[32m~/code/MasteringPyTorchV3/.venv/lib/python3.11/site-packages/torchvision/datasets/folder.py:231[39m, in [36mDatasetFolder.__getitem__[39m[34m(self, index)[39m
[32m    229[39m sample = [38;5;28mself[39m.loader(path)
[32m    230[39m [38;5;28;01mif[39;00m [38;5;28mself[39m.transform [38;5;129;01mis[39;00m [38;5;129;01mnot[39;00m [38;5;28;01mNone[39;00m:
[32m--> [39m[32m231[39m     sample = [30;43mself[39;49m[30;43m.[39;49m[30;43mtransform[39;49m[30;43m([39;49m[30;43msample[39;49m[30;43m)[39;49m
[32m    232[39m [38;5;28;01mif[39;00m [38;5;28mself[39m.target_transform [38;5;129;01mis[39;00m [38;5;129;01mnot[39;00m [38;5;28;01mNone[39;00m:
[32m    233[39m     target = [38;5;28mself[39m.target_transform(target)

[36mFile [39m[32m~/code/MasteringPyTorchV3/.venv/lib/python3.11/site-packages/torchvision/transforms/transforms.py:95[39m, in [36mCompose.__call__[39m[34m(self, img)[39m
[32m     93[39m [38;5;28;01mdef[39;00m[38;5;250m [39m[34m__call__[39m([38;5;28mself[39m, img):
[32m     94[39m     [38;5;28;01mfor[39;00m t [38;5;129;01min[39;00m [38;5;28mself[39m.transforms:
[32m---> [39m[32m95[39m         img = [30;43mt[39;49m[30;43m([39;49m[30;43mimg[39;49m[30;43m)[39;49m
[32m     96[39m     [38;5;28;01mreturn[39;00m img

[36mFile [39m[32m~/code/MasteringPyTorchV3/.venv/lib/python3.11/site-packages/torchvision/transforms/transforms.py:137[39m, in [36mToTensor.__call__[39m[34m(self, pic)[39m
[32m    129[39m [38;5;28;01mdef[39;00m[38;5;250m [39m[34m__call__[39m([38;5;28mself[39m, pic):
[32m    130[39m [38;5;250m    [39m[33;03m"""[39;00m
[32m    131[39m [33;03m    Args:[39;00m
[32m    132[39m [33;03m        pic (PIL Image or numpy.ndarray): Image to be converted to tensor.[39;00m
[32m   (...)[39m[32m    135[39m [33;03m        Tensor: Converted image.[39;00m
[32m    136[39m [33;03m    """[39;00m
[32m--> [39m[32m137[39m     [38;5;28;01mreturn[39;00m [30;43mF[39;49m[30;43m.[39;49m[30;43mto_tensor[39;49m[30;43m([39;49m[30;43mpic[39;49m[30;43m)[39;49m

[36mFile [39m[32m~/code/MasteringPyTorchV3/.venv/lib/python3.11/site-packages/torchvision/transforms/functional.py:167[39m, in [36mto_tensor[39m[34m(pic)[39m
[32m    165[39m [38;5;66;03m# handle PIL Image[39;00m
[32m    166[39m mode_to_nptype = {[33m"[39m[33mI[39m[33m"[39m: np.int32, [33m"[39m[33mI;16[39m[33m"[39m [38;5;28;01mif[39;00m sys.byteorder == [33m"[39m[33mlittle[39m[33m"[39m [38;5;28;01melse[39;00m [33m"[39m[33mI;16B[39m[33m"[39m: np.int16, [33m"[39m[33mF[39m[33m"[39m: np.float32}
[32m--> [39m[32m167[39m img = [30;43mtorch[39;49m[30;43m.[39;49m[30;43mfrom_numpy[39;49m[30;43m([39;49m[30;43mnp[39;49m[30;43m.[39;49m[30;43marray[39;49m[30;43m([39;49m[30;43mpic[39;49m[30;43m,[39;49m[30;43m [39;49m[30;43mmode_to_nptype[39;49m[30;43m.[39;49m[30;43mget[39;49m[30;43m([39;49m[30;43mpic[39;49m[30;43m.[39;49m[30;43mmode[39;49m[30;43m,[39;49m[30;43m [39;49m[30;43mnp[39;49m[30;43m.[39;49m[30;43muint8[39;49m[30;43m)[39;49m[30;43m,[39;49m[30;43m [39;49m[30;43mcopy[39;49m[30;43m=[39;49m[30;43;01mTrue[39;49;00m[30;43m)[39;49m[30;43m)[39;49m
[32m    169[39m [38;5;28;01mif[39;00m pic.mode == [33m"[39m[33m1[39m[33m"[39m:
[32m    170[39m     img = [32m255[39m * img

[31mRuntimeError[39m: Numpy is not available


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
visualize_predictions(model)
------------------

----- stderr -----

A module that was compiled using NumPy 1.x cannot be run in
NumPy 2.4.6 as it may crash. To support both 1.x and 2.x
versions of NumPy, modules must be compiled with NumPy 2.0.
Some module may need to rebuild instead e.g. with 'pybind11>=2.12'.

If you are a user of the module, the easiest solution will be to
downgrade to 'numpy<2' or try to upgrade the affected module.
We expect that some modules will need time to support NumPy 2.

Traceback (most recent call last):  File "<string>", line 1, in <module>
  File "/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/multiprocessing/spawn.py", line 122, in spawn_main
    exitcode = _main(fd, parent_sentinel)
  File "/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/multiprocessing/spawn.py", line 132, in _main
    self = reduction.pickle.load(from_parent)
  File "/Users/ashish/code/MasteringPyTorchV3/.venv/lib/python3.11/site-packages/torch/__init__.py", line 1471, in <module>
    from .functional import *  # noqa: F403
  File "/Users/ashish/code/MasteringPyTorchV3/.venv/lib/python3.11/site-packages/torch/functional.py", line 9, in <module>
    import torch.nn.functional as F
  File "/Users/ashish/code/MasteringPyTorchV3/.venv/lib/python3.11/site-packages/torch/nn/__init__.py", line 1, in <module>
    from .modules import *  # noqa: F403
  File "/Users/ashish/code/MasteringPyTorchV3/.venv/lib/python3.11/site-packages/torch/nn/modules/__init__.py", line 35, in <module>
    from .transformer import TransformerEncoder, TransformerDecoder, \
  File "/Users/ashish/code/MasteringPyTorchV3/.venv/lib/python3.11/site-packages/torch/nn/modules/transformer.py", line 20, in <module>
    device: torch.device = torch.device(torch._C._get_default_device()),  # torch.device('cpu'),

A module that was compiled using NumPy 1.x cannot be run in
NumPy 2.4.6 as it may crash. To support both 1.x and 2.x
versions of NumPy, modules must be compiled with NumPy 2.0.
Some module may need to rebuild instead e.g. with 'pybind11>=2.12'.

If you are a user of the module, the easiest solution will be to
downgrade to 'numpy<2' or try to upgrade the affected module.
We expect that some modules will need time to support NumPy 2.

Traceback (most recent call last):  File "<string>", line 1, in <module>
  File "/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/multiprocessing/spawn.py", line 122, in spawn_main
    exitcode = _main(fd, parent_sentinel)
  File "/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/multiprocessing/spawn.py", line 132, in _main
    self = reduction.pickle.load(from_parent)
  File "/Users/ashish/code/MasteringPyTorchV3/.venv/lib/python3.11/site-packages/torch/__init__.py", line 1471, in <module>
    from .functional import *  # noqa: F403
  File "/Users/ashish/code/MasteringPyTorchV3/.venv/lib/python3.11/site-packages/torch/functional.py", line 9, in <module>
    import torch.nn.functional as F
  File "/Users/ashish/code/MasteringPyTorchV3/.venv/lib/python3.11/site-packages/torch/nn/__init__.py", line 1, in <module>
    from .modules import *  # noqa: F403
  File "/Users/ashish/code/MasteringPyTorchV3/.venv/lib/python3.11/site-packages/torch/nn/modules/__init__.py", line 35, in <module>
    from .transformer import TransformerEncoder, TransformerDecoder, \
  File "/Users/ashish/code/MasteringPyTorchV3/.venv/lib/python3.11/site-packages/torch/nn/modules/transformer.py", line 20, in <module>
    device: torch.device = torch.device(torch._C._get_default_device()),  # torch.device('cpu'),
/Users/ashish/code/MasteringPyTorchV3/.venv/lib/python3.11/site-packages/torch/nn/modules/transformer.py:20: UserWarning: Failed to initialize NumPy: _ARRAY_API not found (Triggered internally at /Users/runner/work/pytorch/pytorch/pytorch/torch/csrc/utils/tensor_numpy.cpp:84.)
  device: torch.device = torch.device(torch._C._get_default_device()),  # torch.device('cpu'),
/Users/ashish/code/MasteringPyTorchV3/.venv/lib/python3.11/site-packages/torch/nn/modules/transformer.py:20: UserWarning: Failed to initialize NumPy: _ARRAY_API not found (Triggered internally at /Users/runner/work/pytorch/pytorch/pytorch/torch/csrc/utils/tensor_numpy.cpp:84.)
  device: torch.device = torch.device(torch._C._get_default_device()),  # torch.device('cpu'),
----- stderr -----
[transformers] Disabling PyTorch because PyTorch >= 2.4 is required but found 2.2.0
[transformers] Disabling PyTorch because PyTorch >= 2.4 is required but found 2.2.0
----- stderr -----
[transformers] PyTorch was not found. Models won't be available and only tokenizers, configuration and file/data utilities can be used.
[transformers] PyTorch was not found. Models won't be available and only tokenizers, configuration and file/data utilities can be used.
------------------

[31m---------------------------------------------------------------------------[39m
[31mRuntimeError[39m                              Traceback (most recent call last)
[36mCell[39m[36m [39m[32mIn[7][39m[32m, line 1[39m
[32m----> [39m[32m1[39m visualize_predictions(model)

[36mCell[39m[36m [39m[32mIn[5][39m[32m, line 19[39m, in [36mvisualize_predictions[39m[34m(pretrained_model, max_num_imgs)[39m
[32m     15[39m     imgs_counter = [32m0[39m
[32m     16[39m     fig = plt.figure()
[32m     17[39m 
[32m     18[39m     [38;5;28;01mwith[39;00m torch.no_grad():
[32m---> [39m[32m19[39m         [38;5;28;01mfor[39;00m i, (imgs, tgts) [38;5;28;01min[39;00m enumerate(dloaders[[33m'val'[39m]):
[32m     20[39m             imgs = imgs.to(dvc)
[32m     21[39m             ops = pretrained_model(imgs)
[32m     22[39m             _, preds = torch.max(ops, [32m1[39m)

[36mFile [39m[32m~/code/MasteringPyTorchV3/.venv/lib/python3.11/site-packages/torch/utils/data/dataloader.py:631[39m, in [36m_BaseDataLoaderIter.__next__[39m[34m(self)[39m
[32m    628[39m [38;5;28;01mif[39;00m [38;5;28mself[39m._sampler_iter [38;5;129;01mis[39;00m [38;5;28;01mNone[39;00m:
[32m    629[39m     [38;5;66;03m# TODO(https://github.com/pytorch/pytorch/issues/76750)[39;00m
[32m    630[39m     [38;5;28mself[39m._reset()  [38;5;66;03m# type: ignore[call-arg][39;00m
[32m--> [39m[32m631[39m data = [30;43mself[39;49m[30;43m.[39;49m[30;43m_next_data[39;49m[30;43m([39;49m[30;43m)[39;49m
[32m    632[39m [38;5;28mself[39m._num_yielded += [32m1[39m
[32m    633[39m [38;5;28;01mif[39;00m [38;5;28mself[39m._dataset_kind == _DatasetKind.Iterable [38;5;129;01mand[39;00m \
[32m    634[39m         [38;5;28mself[39m._IterableDataset_len_called [38;5;129;01mis[39;00m [38;5;129;01mnot[39;00m [38;5;28;01mNone[39;00m [38;5;129;01mand[39;00m \
[32m    635[39m         [38;5;28mself[39m._num_yielded > [38;5;28mself[39m._IterableDataset_len_called:

[36mFile [39m[32m~/code/MasteringPyTorchV3/.venv/lib/python3.11/site-packages/torch/utils/data/dataloader.py:1346[39m, in [36m_MultiProcessingDataLoaderIter._next_data[39m[34m(self)[39m
[32m   1344[39m [38;5;28;01melse[39;00m:
[32m   1345[39m     [38;5;28;01mdel[39;00m [38;5;28mself[39m._task_info[idx]
[32m-> [39m[32m1346[39m     [38;5;28;01mreturn[39;00m [30;43mself[39;49m[30;43m.[39;49m[30;43m_process_data[39;49m[30;43m([39;49m[30;43mdata[39;49m[30;43m)[39;49m

[36mFile [39m[32m~/code/MasteringPyTorchV3/.venv/lib/python3.11/site-packages/torch/utils/data/dataloader.py:1372[39m, in [36m_MultiProcessingDataLoaderIter._process_data[39m[34m(self, data)[39m
[32m   1370[39m [38;5;28mself[39m._try_put_index()
[32m   1371[39m [38;5;28;01mif[39;00m [38;5;28misinstance[39m(data, ExceptionWrapper):
[32m-> [39m[32m1372[39m     [30;43mdata[39;49m[30;43m.[39;49m[30;43mreraise[39;49m[30;43m([39;49m[30;43m)[39;49m
[32m   1373[39m [38;5;28;01mreturn[39;00m data

[36mFile [39m[32m~/code/MasteringPyTorchV3/.venv/lib/python3.11/site-packages/torch/_utils.py:722[39m, in [36mExceptionWrapper.reraise[39m[34m(self)[39m
[32m    718[39m [38;5;28;01mexcept[39;00m [38;5;167;01mTypeError[39;00m:
[32m    719[39m     [38;5;66;03m# If the exception takes multiple arguments, don't try to[39;00m
[32m    720[39m     [38;5;66;03m# instantiate since we don't know how to[39;00m
[32m    721[39m     [38;5;28;01mraise[39;00m [38;5;167;01mRuntimeError[39;00m(msg) [38;5;28;01mfrom[39;00m[38;5;250m [39m[38;5;28;01mNone[39;00m
[32m--> [39m[32m722[39m [38;5;28;01mraise[39;00m exception

[31mRuntimeError[39m: Caught RuntimeError in DataLoader worker process 0.
Original Traceback (most recent call last):
  File "/Users/ashish/code/MasteringPyTorchV3/.venv/lib/python3.11/site-packages/torch/utils/data/_utils/worker.py", line 308, in _worker_loop
    data = fetcher.fetch(index)
           ^^^^^^^^^^^^^^^^^^^^
  File "/Users/ashish/code/MasteringPyTorchV3/.venv/lib/python3.11/site-packages/torch/utils/data/_utils/fetch.py", line 51, in fetch
    data = [self.dataset[idx] for idx in possibly_batched_index]
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/ashish/code/MasteringPyTorchV3/.venv/lib/python3.11/site-packages/torch/utils/data/_utils/fetch.py", line 51, in <listcomp>
    data = [self.dataset[idx] for idx in possibly_batched_index]
            ~~~~~~~~~~~~^^^^^
  File "/Users/ashish/code/MasteringPyTorchV3/.venv/lib/python3.11/site-packages/torchvision/datasets/folder.py", line 231, in __getitem__
    sample = self.transform(sample)
             ^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/ashish/code/MasteringPyTorchV3/.venv/lib/python3.11/site-packages/torchvision/transforms/transforms.py", line 95, in __call__
    img = t(img)
          ^^^^^^
  File "/Users/ashish/code/MasteringPyTorchV3/.venv/lib/python3.11/site-packages/torchvision/transforms/transforms.py", line 137, in __call__
    return F.to_tensor(pic)
           ^^^^^^^^^^^^^^^^
  File "/Users/ashish/code/MasteringPyTorchV3/.venv/lib/python3.11/site-packages/torchvision/transforms/functional.py", line 167, in to_tensor
    img = torch.from_numpy(np.array(pic, mode_to_nptype.get(pic.mode, np.uint8), copy=True))
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
RuntimeError: Numpy is not available



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

### `Chapter15/pytorch_lightning.ipynb`
```
Traceback (most recent call last):
  File "/Users/ashish/code/MasteringPyTorchV3/.venv/lib/python3.11/site-packages/nbclient/client.py", line 657, in async_setup_kernel
    raise e
  File "/Users/ashish/code/MasteringPyTorchV3/.venv/lib/python3.11/site-packages/nbclient/client.py", line 654, in async_setup_kernel
    yield
  File "/Users/ashish/code/MasteringPyTorchV3/.venv/lib/python3.11/site-packages/nbclient/client.py", line 709, in async_execute
    await self.async_execute_cell(
  File "/Users/ashish/code/MasteringPyTorchV3/.venv/lib/python3.11/site-packages/nbclient/client.py", line 1009, in async_execute_cell
    raise DeadKernelError("Kernel died") from None
nbclient.exceptions.DeadKernelError: Kernel died

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/Users/ashish/code/MasteringPyTorchV3/scripts/validate_notebooks.py", line 85, in run_one
    client.execute()
  File "/Users/ashish/code/MasteringPyTorchV3/.venv/lib/python3.11/site-packages/jupyter_core/utils/__init__.py", line 165, in wrapped
    return loop.run_until_complete(inner)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/asyncio/base_events.py", line 654, in run_until_complete
    return future.result()
           ^^^^^^^^^^^^^^^
  File "/Users/ashish/code/MasteringPyTorchV3/.venv/lib/python3.11/site-packages/nbclient/client.py", line 693, in async_execute
    async with self.async_setup_kernel(**kwargs):
  File "/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/contextlib.py", line 231, in __aexit__
    await self.gen.athrow(typ, value, traceback)
  File "/Users/ashish/code/MasteringPyTorchV3/.venv/lib/python3.11/site-packages/nbclient/client.py", line 660, in async_setup_kernel
    await self._async_cleanup_kernel()
  File "/Users/ashish/code/MasteringPyTorchV3/.venv/lib/python3.11/site-packages/nbclient/client.py", line 504, in _async_cleanup_kernel
    assert self.km is not None
           ^^^^^^^^^^^^^^^^^^^
AssertionError

```

### `Chapter15/pytorch_profiler.ipynb`
```
Traceback (most recent call last):
  File "/Users/ashish/code/MasteringPyTorchV3/.venv/lib/python3.11/site-packages/nbclient/client.py", line 657, in async_setup_kernel
    raise e
  File "/Users/ashish/code/MasteringPyTorchV3/.venv/lib/python3.11/site-packages/nbclient/client.py", line 654, in async_setup_kernel
    yield
  File "/Users/ashish/code/MasteringPyTorchV3/.venv/lib/python3.11/site-packages/nbclient/client.py", line 709, in async_execute
    await self.async_execute_cell(
  File "/Users/ashish/code/MasteringPyTorchV3/.venv/lib/python3.11/site-packages/nbclient/client.py", line 1009, in async_execute_cell
    raise DeadKernelError("Kernel died") from None
nbclient.exceptions.DeadKernelError: Kernel died

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/Users/ashish/code/MasteringPyTorchV3/scripts/validate_notebooks.py", line 85, in run_one
    client.execute()
  File "/Users/ashish/code/MasteringPyTorchV3/.venv/lib/python3.11/site-packages/jupyter_core/utils/__init__.py", line 165, in wrapped
    return loop.run_until_complete(inner)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/asyncio/base_events.py", line 654, in run_until_complete
    return future.result()
           ^^^^^^^^^^^^^^^
  File "/Users/ashish/code/MasteringPyTorchV3/.venv/lib/python3.11/site-packages/nbclient/client.py", line 693, in async_execute
    async with self.async_setup_kernel(**kwargs):
  File "/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/contextlib.py", line 231, in __aexit__
    await self.gen.athrow(typ, value, traceback)
  File "/Users/ashish/code/MasteringPyTorchV3/.venv/lib/python3.11/site-packages/nbclient/client.py", line 660, in async_setup_kernel
    await self._async_cleanup_kernel()
  File "/Users/ashish/code/MasteringPyTorchV3/.venv/lib/python3.11/site-packages/nbclient/client.py", line 504, in _async_cleanup_kernel
    assert self.km is not None
           ^^^^^^^^^^^^^^^^^^^
AssertionError

```

### `Chapter17/captum_interpretability.ipynb`
```
Traceback (most recent call last):
  File "/Users/ashish/code/MasteringPyTorchV3/.venv/lib/python3.11/site-packages/nbclient/client.py", line 657, in async_setup_kernel
    raise e
  File "/Users/ashish/code/MasteringPyTorchV3/.venv/lib/python3.11/site-packages/nbclient/client.py", line 654, in async_setup_kernel
    yield
  File "/Users/ashish/code/MasteringPyTorchV3/.venv/lib/python3.11/site-packages/nbclient/client.py", line 709, in async_execute
    await self.async_execute_cell(
  File "/Users/ashish/code/MasteringPyTorchV3/.venv/lib/python3.11/site-packages/nbclient/client.py", line 1009, in async_execute_cell
    raise DeadKernelError("Kernel died") from None
nbclient.exceptions.DeadKernelError: Kernel died

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/Users/ashish/code/MasteringPyTorchV3/scripts/validate_notebooks.py", line 85, in run_one
    client.execute()
  File "/Users/ashish/code/MasteringPyTorchV3/.venv/lib/python3.11/site-packages/jupyter_core/utils/__init__.py", line 165, in wrapped
    return loop.run_until_complete(inner)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/asyncio/base_events.py", line 654, in run_until_complete
    return future.result()
           ^^^^^^^^^^^^^^^
  File "/Users/ashish/code/MasteringPyTorchV3/.venv/lib/python3.11/site-packages/nbclient/client.py", line 693, in async_execute
    async with self.async_setup_kernel(**kwargs):
  File "/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/contextlib.py", line 231, in __aexit__
    await self.gen.athrow(typ, value, traceback)
  File "/Users/ashish/code/MasteringPyTorchV3/.venv/lib/python3.11/site-packages/nbclient/client.py", line 660, in async_setup_kernel
    await self._async_cleanup_kernel()
  File "/Users/ashish/code/MasteringPyTorchV3/.venv/lib/python3.11/site-packages/nbclient/client.py", line 504, in _async_cleanup_kernel
    assert self.km is not None
           ^^^^^^^^^^^^^^^^^^^
AssertionError

```

### `Chapter17/pytorch_interpretability.ipynb`
```
Traceback (most recent call last):
  File "/Users/ashish/code/MasteringPyTorchV3/.venv/lib/python3.11/site-packages/nbclient/client.py", line 657, in async_setup_kernel
    raise e
  File "/Users/ashish/code/MasteringPyTorchV3/.venv/lib/python3.11/site-packages/nbclient/client.py", line 654, in async_setup_kernel
    yield
  File "/Users/ashish/code/MasteringPyTorchV3/.venv/lib/python3.11/site-packages/nbclient/client.py", line 709, in async_execute
    await self.async_execute_cell(
  File "/Users/ashish/code/MasteringPyTorchV3/.venv/lib/python3.11/site-packages/nbclient/client.py", line 1009, in async_execute_cell
    raise DeadKernelError("Kernel died") from None
nbclient.exceptions.DeadKernelError: Kernel died

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/Users/ashish/code/MasteringPyTorchV3/scripts/validate_notebooks.py", line 85, in run_one
    client.execute()
  File "/Users/ashish/code/MasteringPyTorchV3/.venv/lib/python3.11/site-packages/jupyter_core/utils/__init__.py", line 165, in wrapped
    return loop.run_until_complete(inner)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/asyncio/base_events.py", line 654, in run_until_complete
    return future.result()
           ^^^^^^^^^^^^^^^
  File "/Users/ashish/code/MasteringPyTorchV3/.venv/lib/python3.11/site-packages/nbclient/client.py", line 693, in async_execute
    async with self.async_setup_kernel(**kwargs):
  File "/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/contextlib.py", line 231, in __aexit__
    await self.gen.athrow(typ, value, traceback)
  File "/Users/ashish/code/MasteringPyTorchV3/.venv/lib/python3.11/site-packages/nbclient/client.py", line 660, in async_setup_kernel
    await self._async_cleanup_kernel()
  File "/Users/ashish/code/MasteringPyTorchV3/.venv/lib/python3.11/site-packages/nbclient/client.py", line 504, in _async_cleanup_kernel
    assert self.km is not None
           ^^^^^^^^^^^^^^^^^^^
AssertionError

```

