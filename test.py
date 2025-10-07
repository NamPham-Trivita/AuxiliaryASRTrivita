from models import build_model
import yaml
import torch
config = yaml.safe_load(open("Configs/config.yml"))

model = build_model(model_params=config['model_params'] or {})
print(torch.load("Data/epoch_00080.pth",map_location="cpu",weights_only=False).keys())
model.load_state_dict(torch.load("Data/epoch_00080.pth",map_location="cpu")["model"])

audio_path = "Data/sample_audio.wav"
