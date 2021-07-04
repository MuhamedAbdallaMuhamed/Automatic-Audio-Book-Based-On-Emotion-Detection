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
import 'signin_screen.dart';

class EnterNewPasswordScreen extends StatefulWidget {
  final String email;

  const EnterNewPasswordScreen({Key key, this.email}) : super(key: key);
  @override
  _EnterNewPasswordScreenState createState() => _EnterNewPasswordScreenState();
}

class _EnterNewPasswordScreenState extends State<EnterNewPasswordScreen> {
  final userController = Get.find<UserController>();

  final GlobalKey<FormState> _formKey = GlobalKey<FormState>();

  final TextEditingController code = TextEditingController();

  final TextEditingController password = TextEditingController();
  final TextEditingController confirmPassword = TextEditingController();

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
                    'Code',
                    style: TextStyle(
                      fontSize: 18.sp(context),
                      fontFamily: Keys.Araboto,
                    ),
                  ),
                  TextInput(
                    validate: TextInput.validateText,
                    controller: code,
                  ),
                  Text(
                    'Password',
                    style: TextStyle(
                      fontSize: 18.sp(context),
                      fontFamily: Keys.Araboto,
                    ),
                  ),
                  TextInput(
                    obscure: true,
                    validate: (value) {
                      if (value.isEmpty)
                        return 'Please enter the required information'.tr;
                      if (value.length < 8)
                        return 'Password is too short';
                      else if (value != confirmPassword.text)
                        return "password doesn't match";
                      return null;
                    },
                    controller: password,
                  ),
                  SizedBox(
                    height: 1.heightPercentage(context),
                  ),
                  Text(
                    'Confirm Password',
                    style: TextStyle(
                      fontSize: 18.sp(context),
                      fontFamily: Keys.Araboto,
                    ),
                  ),
                  TextInput(
                    obscure: true,
                    validate: (value) {
                      if (value.isEmpty)
                        return 'Please enter the required information'.tr;
                      if (value.length < 8)
                        return 'Password is too short';
                      else if (value != password.text)
                        return "password doesn't match";
                      return null;
                    },
                    controller: confirmPassword,
                  ),
                  SizedBox(
                    height: 1.heightPercentage(context),
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
                      Result result = await userController.resetPassword(
                          code: code.text,
                          email: widget.email,
                          password: password.text);
                      if (result is SuccessResult) {
                        loading = false;
                        await Get.defaultDialog(
                            middleText: 'Password reset successfully');
                        Get.offAll(SigninScreen());
                      } else {
                        await Get.defaultDialog(
                            middleText: result.getErrorMessage());
                        setState(() {
                          loading = false;
                        });
                      }
                    },
                    textcolor: Colors.white,
                    title: 'Reset Password',
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
