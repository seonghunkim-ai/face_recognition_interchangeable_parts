# face_recognition_interchangeable_parts

기존의 [face_recognition] 에서 image_scrapper, crop_image 파일을 수정하였습니다.

[face_recognition]: https://github.com/seonghunkim-ai/face_recognition

## requirements
VS, CUDA, cuDNN, openCV를 설치합니다.

참고 (실행한 환경)
  - Windows 10 Home
  - i5 7300hq
  - 8gb ddr4
  - gtx1050 2gb
_________________________________________________________________________________
  - Visual Studio 2017 [설치 링크 1] [ [참조 링크 1],  [참조 링크 2] ]
  - CUDA 10.2  [설치 링크 2]
  - cuDNN 7.6.5 for CUDA 10.2  [설치 링크 3] 
    - 압축을 풀고 생성된 디렉터리들을 CUDA 설치 디렉터리에 복사합니다. 
    - ex) C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v10.2)
  - OpenCV 2.4.13.6 [설치 링크 4]
    - 압축을 풀고 생성된 폴더를 C: 에 위치시킵니다. 폴더이름은 opencv로 지정합니다.
    ![a.png](./image/a.png)
    - 시스템 환경 변수에 OPENCV_DIR 이름으로 opencv path를 등록합니다.
  
[darknet]: https://github.com/AlexeyAB/darknet/
[설치 링크 1]: https://docs.microsoft.com/ko-kr/visualstudio/releasenotes/vs2017-relnotes
[설치 링크 2]: https://developer.nvidia.com/cuda-downloads
[설치 링크 3]: https://developer.nvidia.com/rdp/form/cudnn-download-survey
[설치 링크 4]: https://opencv.org/releases/

[참조 링크 1]: https://murra.tistory.com/100
[참조 링크 2]: https://todaybbs.tistory.com/2


## training data
10명의 학생 얼굴 이미지 4500여장을 학습시켰습니다. (명당 4~500장) 

