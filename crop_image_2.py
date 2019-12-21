import cv2
import os
import pathlib
import dlib
import openface


file_path = '../original_test_image'
classifier_path = './cascade_classifier/'
predictor_model = classifier_path + "shape_predictor_68_face_landmarks.dat"

face_detector = dlib.get_frontal_face_detector()
face_pose_predictor = dlib.shape_predictor(predictor_model)
face_aligner = openface.AlignDlib(predictor_model)


def align_face(img, img_dim):
    assert img is not None

    detected_faces = face_detector(img, 1)

    aligned_face_list = []

    if len(detected_faces) >= 1:

        for face in detected_faces:
            face_rect = face

            aligned_face = face_aligner.align(534, img, face_rect, landmarkIndices=openface.AlignDlib.OUTER_EYES_AND_NOSE)

            aligned_face_list.append(cv2.resize(aligned_face, (img_dim, img_dim)))

    return aligned_face_list


def cropping():
    for directoryName in os.listdir(file_path):
        celeb_name = directoryName
        cascade_path = '../cropped_test_image/' + celeb_name
        pathlib.Path(cascade_path).mkdir(parents=True, exist_ok=True)

        for fileName in os.listdir(file_path + '/' + celeb_name):
            image_name = cv2.imread(file_path + '/' + celeb_name + '/' + fileName)
            print(fileName)
            aligned = align_face(image_name, 224)
            os.chdir(cascade_path)

            if len(aligned) is 1:
                cv2.imwrite(fileName, aligned[0])
            else:
                sub_num = 1
                fileName, fileType = fileName.split('.')
                for img in aligned:
                    sub_fileName = fileName + '_' + str(sub_num) + '.' + fileType
                    cv2.imwrite(sub_fileName, img)
                    sub_num += 1
            os.chdir('../../face_recognition')


if __name__ == '__main__':
    cropping()
