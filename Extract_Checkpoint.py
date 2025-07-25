import torch

# Define Args class BEFORE loading the checkpoint
class Args:
    # Training config
    batch_size = 2
    test_batch_size = 4
    vit_pretrain_path = 'pretrained-weights/mae_pretrain_vit_base.pth'
    epochs = 100
    test_period = 4
    accum_iter = 8
    edge_broaden = 7
    edge_lambda = 20
    predict_head_norm = "BN"

    # Optimizer config
    weight_decay = 0.05
    lr = None
    blr = 1e-3
    min_lr = 0.0
    warmup_epochs = 4
    opt = 'AdamW'
    betas = (0.9, 0.999)
    momentum = 0.9

    # Dataset
    data_path = 'CASIA2.0'
    test_data_path = 'CASIA1.0'

    # System and logging
    output_dir = './output_dir'
    log_dir = './output_dir'
    device = torch.device('cuda')
    seed = 42
    resume = ''
    start_epoch = 0
    num_workers = 4
    pin_mem = True
    distributed = False
    gpu = 0
    world_size = 1
    local_rank = -1
    dist_on_itp = False
    dist_url = 'env://'

# Now load the checkpoint
checkpoint = torch.load("output_dir/512 Size 100 Epochs/checkpoint-99.pth", weights_only=False)
model_state = checkpoint['model']
torch.save(model_state, "checkpoints/iml-vit_checkpoint-99-512.pth")
print("✅ Weights-only checkpoint saved.")
