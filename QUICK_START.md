# Quick Start Guide

Get up and running with Deep-Live-Cam in minutes!

## ⚡ Fast Track (3 Steps)

### Step 1: Setup (5 minutes)

```bash
# Clone the repository
git clone https://github.com/hacksider/Deep-Live-Cam.git
cd Deep-Live-Cam

# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### Step 2: Download Models (5 minutes)

Download these two files and place them in the `models/` folder:

1. **inswapper_128_fp16.onnx** (~256 MB)
   - https://huggingface.co/hacksider/deep-live-cam/resolve/main/inswapper_128_fp16.onnx

2. **GFPGANv1.4.pth** (~348 MB)  
   - https://huggingface.co/hacksider/deep-live-cam/resolve/main/GFPGANv1.4.pth

```bash
# Quick download with wget (if available)
wget -P models/ https://huggingface.co/hacksider/deep-live-cam/resolve/main/inswapper_128_fp16.onnx
wget -P models/ https://huggingface.co/hacksider/deep-live-cam/resolve/main/GFPGANv1.4.pth
```

### Step 3: Run!

```bash
python run.py
```

Then:
1. Click **"Select a face"** → Choose your source image (the face to use)
2. Click **"Select a target"** → Choose your video or image
3. Click **"Start"** → Wait for processing
4. Done! Find your output in the target file's directory

## 🎯 What Each Button Does

| Button | What it does |
|--------|-------------|
| **Select a face** | Choose the face image to swap INTO the video |
| **Select a target** | Choose the video/image where faces will be replaced |
| **Start** | Begin processing video/image |
| **Live** | Start real-time webcam face swap |
| **Face Enhancer** | Enable for better quality (slower) |
| **Many Faces** | Swap ALL faces in frame, not just one |

## 📹 Quick Examples

### Example 1: Swap Face in Video
```
Source: my_face.jpg  (your photo)
Target: movie_clip.mp4  (any video)
Result: Your face appears in the movie!
```

### Example 2: Live Webcam Swap
```
1. python run.py
2. Select face image
3. Click "Live"
4. Your face is swapped in real-time!
```

### Example 3: Command Line
```bash
python run.py \
  --source my_face.jpg \
  --target video.mp4 \
  --output result.mp4
```

## ✅ Verification

After cloning, verify everything works:

```bash
# Install test dependencies
pip install -r requirements-dev.txt

# Run tests
python run_tests.py

# See workflow demo
python examples/demo_workflow.py
```

Expected output: `16 passed, 2 skipped` ✓

## 🚀 Performance Tips

### Use GPU Acceleration (10-50x faster!)

**NVIDIA GPU (CUDA):**
```bash
python run.py --execution-provider cuda
```

**AMD GPU (DirectML on Windows):**
```bash
python run.py --execution-provider directml
```

**Mac Silicon (M1/M2/M3):**
```bash
python run.py --execution-provider coreml
```

## 📚 Learn More

- **Detailed Usage Guide:** [examples/USAGE_GUIDE.md](examples/USAGE_GUIDE.md)
- **Testing Guide:** [TESTING.md](TESTING.md)
- **Full README:** [README.md](README.md)
- **Contributing:** [CONTRIBUTING.md](CONTRIBUTING.md)

## ⚠️ Important Notes

- ✅ Get consent before using someone's face
- ✅ Label outputs as deepfakes when sharing
- ✅ Use responsibly and ethically
- ❌ Don't create inappropriate content
- ❌ Don't use for fraud or deception

## 🆘 Troubleshooting

**"Model file not found"**
→ Download models (Step 2 above)

**"No face detected"**  
→ Use clearer photos with visible faces

**Very slow processing**
→ Enable GPU acceleration (see Performance Tips)

**Import errors**
→ Make sure you activated the venv and installed requirements

**Need help?**
→ Open an issue on GitHub!

---

**That's it! You're ready to start swapping faces! 🎭**
