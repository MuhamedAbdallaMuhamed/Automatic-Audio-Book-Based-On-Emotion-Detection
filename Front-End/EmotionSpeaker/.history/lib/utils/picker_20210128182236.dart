import 'package:flutter/material.dart';
import 'package:EmotionSpeaker/constants/custom_colors.dart';
import 'package:image_picker/image_picker.dart';
import 'package:image_cropper/image_cropper.dart';
import 'dart:io';
import 'package:file_picker/file_picker.dart';

class Picker {
  static ImagePicker picker = ImagePicker();
  static Future<File> pickImage() async {
    File image;
    final PickedFile pickedFile = await picker.getImage(
      source: ImageSource.gallery,
    );
    image = File(pickedFile.path);
    return image;
  }

  static Future<File> cropImage(File image) async {
    File croppedFile = await ImageCropper.cropImage(
      sourcePath: image.path,
      maxHeight: 400,
      maxWidth: 400,
      cropStyle: CropStyle.circle,
      compressFormat: ImageCompressFormat.png,
      aspectRatioPresets: Platform.isAndroid
          ? [
              CropAspectRatioPreset.square,
              CropAspectRatioPreset.ratio3x2,
              CropAspectRatioPreset.original,
              CropAspectRatioPreset.ratio4x3,
              CropAspectRatioPreset.ratio16x9
            ]
          : [
              CropAspectRatioPreset.original,
              CropAspectRatioPreset.square,
              CropAspectRatioPreset.ratio3x2,
              CropAspectRatioPreset.ratio4x3,
              CropAspectRatioPreset.ratio5x3,
              CropAspectRatioPreset.ratio5x4,
              CropAspectRatioPreset.ratio7x5,
              CropAspectRatioPreset.ratio16x9
            ],
      androidUiSettings: AndroidUiSettings(
          toolbarTitle: 'Cropper',
          toolbarColor: CustomColors.color1,
          toolbarWidgetColor: Colors.white,
          initAspectRatio: CropAspectRatioPreset.square,
          lockAspectRatio: false),
      iosUiSettings: IOSUiSettings(
        title: 'Cropper',
      ),
    );
    if (croppedFile != null) {
      image = croppedFile;
    }
    return image;
  }

  static Future<void> pickFile(List<File> doc) async {
    FilePickerResult result = await FilePicker.platform.pickFiles();
    doc.add(File(result.files.single.path));
  }
}
