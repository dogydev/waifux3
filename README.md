# waifux3
Uses StyleGAN 2 to generate waifu pictures 
# Disclaimer
Huge credit goes to the developers of StyleGAN2(https://github.com/NVlabs/stylegan2) and Waifu2x_Chainer(https://github.com/tsurumeso/waifu2x-chainer)
# How to run
Download the pretrained model here(https://drive.google.com/file/d/1wrOzXM0qh3iEujr5CB1tvtsUZuuqR4eY/view?usp=sharing) and run "python generate.py --outdir=out --trunc=1 --seeds=85,265,297,849     --network=$PRETRAINED_MODEL
# Training
To train, follow steps on the original StyleGAN2 repo but use the Anine Faces(https://www.kaggle.com/splcher/animefacedataset) dataset. Use the rescaler.py to normalize all the images before parsing them to the trainer.
