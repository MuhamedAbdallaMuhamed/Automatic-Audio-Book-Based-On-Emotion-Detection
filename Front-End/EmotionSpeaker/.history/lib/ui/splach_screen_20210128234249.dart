import 'package:EmotionSpeaker/constants/custom_colors.dart';
import 'package:EmotionSpeaker/constants/keys.dart';
import 'package:EmotionSpeaker/controller/user_controller.dart';
import 'package:EmotionSpeaker/models/result.dart';
import 'package:EmotionSpeaker/ui/home_screen.dart';
import 'package:EmotionSpeaker/ui/register_or_login_screen.dart';
import 'package:flutter/material.dart';
import 'package:get/get.dart';
import 'package:EmotionSpeaker/utils/sizing_extension.dart';

class SplachScreen extends StatefulWidget {
  static const String Route_Name = 'SplachScreen';
  @override
  _SplachScreenState createState() => _SplachScreenState();
}

class _SplachScreenState extends State<SplachScreen> {
  final userController = Get.put(UserController());
  @override
  void initState() {
    super.initState();
    Future.delayed(Duration(seconds: 5), () async {
      Result result = await userController.openApp();
      if (result is SuccessResult)
        Get.offAll(HomeScreen());
      else {
        if (result.getErrorMessage() == Keys.Logout) {
          Get.offAll(RegisterOrLoginScreen());
        } else
          Get.defaultDialog(
            title: 'Error',
          );
      }
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: CustomColors.backgroundColor,
      body: Hero(
        tag: '1',
        child: Center(
          child: Image.asset(
            'assets/audiobook.png',
            height: 50.widthPercentage(context),
            width: 50.widthPercentage(context),
          ),
        ),
      ),
    );
  }
}
