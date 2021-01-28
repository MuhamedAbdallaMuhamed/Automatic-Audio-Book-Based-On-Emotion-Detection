import 'package:EmotionSpeaker/constants/custom_colors.dart';
import 'package:EmotionSpeaker/controller/user_controller.dart';
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
  @override
  void initState() {
    super.initState();
    Future.delayed(Duration(seconds: 5), () async {
      Get.put(UserController());
      Get.offAll(RegisterOrLoginScreen());
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
