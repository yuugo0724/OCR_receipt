# SwinIR
実行方法
```
python main_test_swinir.py --task real_sr --scale 4 --large_model --model_path model_zoo/swinir/003_realSR_BSRGAN_DFOWMFC_s64w8_SwinIR-L_x4_GAN.pth --folder_lq testsets/RealSRSet+5images
```
--scale4で4倍の超解像になる  
--folder_lqでフォルダを指定  

高画質化された画像は「results/swinir_real_sr_x4_large」に保存される  

