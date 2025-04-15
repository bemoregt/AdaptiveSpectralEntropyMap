# 적응형 스펙트럴 엔트로피 맵 (Adaptive Spectral Entropy Map)

이미지의 지역적 주파수 특성을 분석하는 스펙트럴 엔트로피 맵 알고리즘입니다.

## 데모 결과

![스펙트럴 엔트로피 맵 시연 결과](ScrShot%202.png)

## 개요

이 알고리즘은 이미지를 작은 블록으로 분할하고, 각 블록에 대해 2차원 푸리에 변환을 적용하여 주파수 도메인의 특성을 분석합니다. 각 블록의 주파수 스펙트럼에서 엔트로피를 계산하여 이미지의 지역적 복잡도를 시각화합니다.

## 특징

- 이미지의 지역적 텍스처 복잡도를 정량화
- 주파수 도메인에서의 정보량 측정
- 적응형 블록 크기 지원 (기본값: 2x2)
- 다양한 이미지 분석 및 세그멘테이션 작업에 활용 가능

## 알고리즘 원리

1. 입력 이미지를 그레이스케일로 변환
2. 이미지를 지정된 크기의 블록으로 분할
3. 각 블록에 대해:
   - 2차원 푸리에 변환(FFT) 수행
   - 진폭 스펙트럼 계산
   - 스펙트럼 정규화
   - 스펙트럴 엔트로피 계산 (-sum(p*log(p)))
4. 계산된 엔트로피 값으로 맵 구성

## 사용법

```python
from spectral_entropy import local_spectral_entropy_map
from skimage import data
import matplotlib.pyplot as plt

# 이미지 로드
image = data.astronaut()

# 스펙트럴 엔트로피 맵 계산
entropy_map = local_spectral_entropy_map(image, block_size=(4, 4))

# 결과 시각화
plt.imshow(entropy_map, cmap='viridis')
plt.colorbar(label='Spectral Entropy')
plt.title("Local Spectral Entropy Map")
plt.show()
```

## 응용 분야

- 이미지 텍스처 분석
- 이미지 세그멘테이션
- 이미지 품질 평가
- 이미지 포렌식
- 생물의학 영상 분석

## 의존성

- NumPy
- SciPy
- scikit-image
- Matplotlib (시각화용)

## 라이선스

MIT License

## 참고 문헌

- Gonzalez, R. C., & Woods, R. E. (2018). Digital image processing. Pearson.
- Humeau-Heurtier, A. (2019). Texture feature extraction methods: A survey. IEEE Access, 7, 8975-9000.