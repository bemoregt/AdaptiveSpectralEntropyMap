import numpy as np
from scipy.fftpack import fft2, fftshift
from skimage.color import rgb2gray
from skimage.util import view_as_blocks

# 스펙트럴 엔트로피 함수
def local_spectral_entropy_map(image, block_size=(2, 2)):
    # 그레이스케일링
    if image.ndim == 3:
        image = rgb2gray(image)
    
    # 이미지를 블럭들로 분할
    blocks = view_as_blocks(image, block_size)
    num_blocks = blocks.shape[0] * blocks.shape[1]
    spectral_entropy_map = np.zeros(image.shape)
    
    # 각 블럭에 대한 spectral entropy 계산
    for i in range(blocks.shape[0]):
        for j in range(blocks.shape[1]):
            block = blocks[i, j]
            # 2차원 푸리에변환
            fft = fft2(block)
            # 진폭 스펙트럼
            magnitude_spectrum = np.abs(fft)
            # 정규화
            magnitude_spectrum /= np.sum(magnitude_spectrum)
            # spectral entropy 계산
            spectral_entropy = -np.sum(magnitude_spectrum * np.log1p(magnitude_spectrum))
            # 각 spectral entropy 를 map에 저장
            spectral_entropy_map[i*block_size[0]:(i+1)*block_size[0], j*block_size[1]:(j+1)*block_size[1]] = spectral_entropy
    
    return spectral_entropy_map

if __name__ == "__main__":
    from skimage import data
    import matplotlib.pyplot as plt

    # 이미지 로딩
    image = data.astronaut() 

    # local 2D spectral entropy map 함수 호출
    spectral_entropy_map = local_spectral_entropy_map(image)

    # 디스플레이
    plt.figure(figsize=(12, 6))
    
    plt.subplot(1, 2, 1)
    plt.imshow(image)
    plt.title("Original Image")
    
    plt.subplot(1, 2, 2)
    plt.imshow(spectral_entropy_map, cmap='viridis')
    plt.colorbar(label='Spectral Entropy')
    plt.title("Local Spectral Entropy Map")
    
    plt.tight_layout()
    plt.show()