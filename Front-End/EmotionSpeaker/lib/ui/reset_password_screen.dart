import 'package:EmotionSpeaker/common_widgets/text_input.dart';
import 'package:EmotionSpeaker/common_widgets/rounded_button.dart';
import 'package:EmotionSpeaker/constants/custom_colors.dart';
import 'package:EmotionSpeaker/constants/keys.dart';
import 'package:EmotionSpeaker/controller/user_controller.dart';
import 'package:EmotionSpeaker/models/result.dart';
import 'package:EmotionSpeaker/ui/home_screen.dart';
import 'package:flutter/material.dart';
import 'package:EmotionSpeaker/utils/sizing_extension.dart';
import 'package:get/get.dart';
import 'package:modal_progress_hud/modal_progress_hud.dart';
import 'package:EmotionSpeaker/ui/enter_new_password_screen.dart';

class ResetPasswordScreen extends StatefulWidget {
  @override
  _ResetPasswordScreenState createState() => _ResetPasswordScreenState();
}

class _ResetPasswordScreenState extends State<ResetPasswordScreen> {
  final userController = Get.find<UserController>();

  final GlobalKey<FormState> _formKey = GlobalKey<FormState>();

  final TextEditingController email = TextEditingController();

  bool loading = false;

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: CustomColors.backgroundColor,
      body: ModalProgressHUD(
        inAsyncCall: loading,
        child: Form(
          key: _formKey,
          child: SingleChildScrollView(
            child: Padding(
              padding: EdgeInsets.symmetric(
                horizontal: 10.widthPercentage(context),
              ),
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.stretch,
                children: [
                  SizedBox(
                    height: 10.heightPercentage(context),
                  ),
                  Center(
                    child: Hero(
                      tag: '1',
                      transitionOnUserGestures: true,
                      child: Image.asset(
                        'assets/audiobook.png',
                        height: 30.widthPercentage(context),
                        width: 30.widthPercentage(context),
                      ),
                    ),
                  ),
                  SizedBox(
                    height: 1.heightPercentage(context),
                  ),
                  Center(
                    child: Text(
                      'Sign In',
                      style: TextStyle(
                        fontSize: 30.sp(context),
                        fontFamily: Keys.Araboto,
                        fontWeight: FontWeight.bold,
                      ),
                    ),
                  ),
                  SizedBox(
                    height: 5.heightPercentage(context),
                  ),
                  Text(
                    'Email',
                    style: TextStyle(
                      fontSize: 18.sp(context),
                      fontFamily: Keys.Araboto,
                    ),
                  ),
                  TextInput(
                    validate: TextInput.validateMail,
                    controller: email,
                  ),
                  SizedBox(
                    height: 2.heightPercentage(context),
                  ),
                  RoundedButton(
                    buttoncolor: CustomColors.color1,
                    onPreesed: () async {
                      if (!_formKey.currentState.validate()) return;
                      setState(() {
                        loading = true;
                      });
                      Result result = await userController.getResetPasswordCode(
                          email: email.text);
                      if (result is SuccessResult) {
                        loading = false;
                        Get.to(EnterNewPasswordScreen(
                          email: email.text,
                        ));
                      } else {
                        await Get.defaultDialog(
                          title: 'Error',
                          middleText: result.getErrorMessage(),
                        );
                        setState(() {
                          loading = false;
                        });
                      }
                    },
                    textcolor: Colors.white,
                    title: 'Send Code',
                  ),
                ],
              ),
            ),
          ),
        ),
      ),
    );
  }

  signinwithGoogle() {
    Get.to(HomeScreen());
  }

  signinwithFacebbok() {
    Get.to(HomeScreen());
  }
}
