# Deep-Live-Cam Usage Guide

This guide shows you how to use Deep-Live-Cam for face swapping in videos and images.

## Prerequisites

Before you start, make sure you have:

1. ✅ Cloned the repository
2. ✅ Installed Python 3.10 or 3.11
3. ✅ Installed dependencies: `pip install -r requirements.txt`
4. ✅ Downloaded the model files (see below)

## Step 1: Download Model Files

You need two model files in the `models` directory:

1. **inswapper_128_fp16.onnx** - The face swapping model
   - Download from: https://huggingface.co/hacksider/deep-live-cam/resolve/main/inswapper_128_fp16.onnx
   - Size: ~256 MB

2. **GFPGANv1.4.pth** - The face enhancement model
   - Download from: https://huggingface.co/hacksider/deep-live-cam/resolve/main/GFPGANv1.4.pth
   - Size: ~348 MB

Place both files in the `models/` directory:

```bash
cd Deep-Live-Cam
# Download models (example using wget)
wget -P models/ https://huggingface.co/hacksider/deep-live-cam/resolve/main/inswapper_128_fp16.onnx
wget -P models/ https://huggingface.co/hacksider/deep-live-cam/resolve/main/GFPGANv1.4.pth
```

## Step 2: Using the GUI Application

### Method 1: Face Swap in Video

1. **Launch the application:**
   ```bash
   python run.py
   ```

2. **Select source face:**
   - Click "Select a face" button
   - Choose an image file with the face you want to use (PNG, JPG, JPEG)
   - This is the face that will be swapped INTO the video

3. **Select target video:**
   - Click "Select a target" button
   - Choose a video file (MP4, MKV)
   - This is the video where faces will be detected and replaced

4. **Configure options (optional):**
   - Enable "Face Enhancer" for better quality output
   - Enable "Many Faces" to swap all detected faces
   - Enable "Map Faces" to map specific source faces to specific target faces

5. **Start processing:**
   - Click "Start" button
   - Wait for processing to complete
   - The output video will be saved in a directory named after your target video

### Method 2: Face Swap in Image

Same steps as video, but select an image as the target instead of a video.

### Method 3: Live Webcam Face Swap

1. **Launch the application:**
   ```bash
   python run.py
   ```

2. **Select source face:**
   - Click "Select a face" button
   - Choose an image file with the face you want to use

3. **Select camera:**
   - Use the camera dropdown to select your webcam

4. **Start live mode:**
   - Click "Live" button
   - Wait 10-30 seconds for initialization
   - Your face will be swapped in real-time!

5. **Stream or record:**
   - Use OBS or similar software to capture the preview window
   - Stream to your favorite platform

## Step 3: Using CLI Mode (Advanced)

For automation or batch processing, use command-line mode:

```bash
# Basic face swap
python run.py \
  --source path/to/source_face.jpg \
  --target path/to/target_video.mp4 \
  --output path/to/output_video.mp4

# With face enhancement
python run.py \
  --source source_face.jpg \
  --target target_video.mp4 \
  --output output_video.mp4 \
  --frame-processor face_swapper face_enhancer

# Process all faces in the video
python run.py \
  --source source_face.jpg \
  --target target_video.mp4 \
  --output output_video.mp4 \
  --many-faces

# Keep original audio and FPS
python run.py \
  --source source_face.jpg \
  --target target_video.mp4 \
  --output output_video.mp4 \
  --keep-fps \
  --keep-audio
```

## Common Use Cases

### 1. Replace Your Face in a Movie Scene

```bash
python run.py
# 1. Select your face photo
# 2. Select the movie clip
# 3. Click "Start"
# Result: You appear in the movie!
```

### 2. Create Memes with Celebrity Faces

```bash
python run.py
# 1. Select celebrity face image
# 2. Select your video
# 3. Enable "Many Faces" if multiple people
# 4. Click "Start"
```

### 3. Anonymous Video Calls

```bash
python run.py
# 1. Select face to use
# 2. Select webcam
# 3. Click "Live"
# 4. Use virtual camera or screen capture in your video call app
```

### 4. Content Creation

```bash
python run.py
# 1. Select character face
# 2. Select your performance video
# 3. Enable "Face Enhancer" for quality
# 4. Click "Start"
# 5. Use output in your content
```

## Tips for Best Results

### Source Face Image
- ✅ Use clear, front-facing photos
- ✅ Good lighting
- ✅ Neutral expression works best
- ✅ High resolution (at least 512x512)
- ❌ Avoid extreme angles
- ❌ Avoid heavy makeup or filters
- ❌ Avoid sunglasses or face coverings

### Target Video
- ✅ Clear face visibility
- ✅ Good lighting
- ✅ Front-facing angles work best
- ❌ Very fast movements may blur
- ❌ Very low quality videos

### Performance
- Use GPU acceleration for faster processing:
  - CUDA (NVIDIA): `python run.py --execution-provider cuda`
  - DirectML (AMD): `python run.py --execution-provider directml`
  - CoreML (Mac): `python run.py --execution-provider coreml`

## Troubleshooting

### "Model file not found"
- Download the model files (see Step 1)
- Verify they're in the `models/` directory

### "No face detected"
- Use a clearer source image with visible face
- Ensure target video has visible faces
- Try different angles or lighting

### Slow processing
- Processing is CPU-intensive without GPU
- Enable GPU acceleration (see Performance tips)
- Reduce video resolution or length for testing

### "Out of memory"
- Reduce `--max-memory` parameter
- Process shorter video clips
- Close other applications
- Use lower resolution videos

## Example Workflow

Here's a complete example from start to finish:

```bash
# 1. Ensure you're in the Deep-Live-Cam directory
cd Deep-Live-Cam

# 2. Verify models are downloaded
ls -l models/
# Should show: GFPGANv1.4.pth, inswapper_128_fp16.onnx

# 3. Prepare your files
# - source_face.jpg: A photo of the face you want to use
# - target_video.mp4: The video where you want to swap faces

# 4. Run the face swap (GUI)
python run.py
# Then use the GUI to select files and start processing

# 5. Or run via CLI
python run.py \
  --source my_photos/source_face.jpg \
  --target my_videos/target_video.mp4 \
  --output results/swapped_video.mp4 \
  --frame-processor face_swapper face_enhancer \
  --keep-fps \
  --keep-audio

# 6. Find your output
# The swapped video will be at: results/swapped_video.mp4
```

## Need Help?

- Check the [main README](../README.md) for installation help
- Review [CONTRIBUTING.md](../CONTRIBUTING.md) for testing guidelines
- Open an issue on GitHub for bugs or questions
- Remember: Use this tool ethically and legally!

## Ethical Reminders

- 🔴 Get consent before using someone's face
- 🔴 Label deepfakes when sharing publicly
- 🔴 Don't create inappropriate or harmful content
- 🔴 Follow all applicable laws and regulations
- ✅ Use for creative and legitimate purposes
- ✅ Respect others' privacy and dignity
