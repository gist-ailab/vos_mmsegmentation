_base_ = [
    '../_base_/models/bisenetv2.py',
    '../_base_/datasets/cityscapes_1024x1024.py',
    '../_base_/default_runtime.py', '../_base_/schedules/schedule_160k.py'
]
sampler = dict(type='OHEMPixelSampler', thresh=0.7, min_kept=10000)
lr_config = dict(warmup='linear', warmup_iters=1000)
optimizer = dict(lr=0.05)
train_dataloader = dict(batch_size=4, num_workers=4)
val_dataloader = dict(batch_size=4, num_workers=4)
test_dataloader = val_dataloader
