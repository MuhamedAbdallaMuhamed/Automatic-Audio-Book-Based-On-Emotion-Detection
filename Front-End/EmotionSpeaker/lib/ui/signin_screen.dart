import 'package:EmotionSpeaker/common_widgets/text_input.dart';
import 'package:EmotionSpeaker/common_widgets/rounded_button.dart';
import 'package:EmotionSpeaker/constants/custom_colors.dart';
import 'package:EmotionSpeaker/constants/keys.dart';
import 'package:EmotionSpeaker/controller/user_controller.dart';
import 'package:EmotionSpeaker/models/result.dart';
import 'package:EmotionSpeaker/models/user.dart';
import 'package:EmotionSpeaker/ui/home_screen.dart';
import 'package:flutter/material.dart';
import 'package:EmotionSpeaker/utils/sizing_extension.dart';
import 'package:get/get.dart';
import 'package:modal_progress_hud/modal_progress_hud.dart';
import 'package:EmotionSpeaker/ui/reset_password_screen.dart';

class SigninScreen extends StatefulWidget {
  @override
  _SigninScreenState createState() => _SigninScreenState();
}

class _SigninScreenState extends State<SigninScreen> {
  final userController = Get.find<UserController>();

  final GlobalKey<FormState> _formKey = GlobalKey<FormState>();

  final TextEditingController email = TextEditingController();

  final TextEditingController password = TextEditingController();

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
                    height: 1.heightPercentage(context),
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
                    validate: TextInput.validateText,
                    controller: password,
                  ),
                  SizedBox(
                    height: 0.1.heightPercentage(context),
                  ),
                  GestureDetector(
                    onTap: () {
                      Get.to(ResetPasswordScreen());
                    },
                    child: Text(
                      'Forget Password',
                      style: TextStyle(
                        fontSize: 18.sp(context),
                        fontFamily: Keys.Araboto,
                        color: CustomColors.color1,
                        decoration: TextDecoration.underline,
                      ),
                    ),
                  ),
                  SizedBox(
                    height: 0.5.heightPercentage(context),
                  ),
                  RoundedButton(
                    title: 'Sign In',
                    buttoncolor: CustomColors.color1,
                    onPreesed: () async {
                      if (!_formKey.currentState.validate()) return;
                      setState(() {
                        loading = true;
                      });
                      String emailStr = email.text;
                      String passwordStr = password.text;
                      User user = User(
                        email: emailStr,
                        password: passwordStr,
                      );
                      Result result =
                          await userController.userLogin(user: user);
                      if (result is SuccessResult) {
                        loading = false;
                        Get.offAll(HomeScreen());
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
                  ),
                  SizedBox(
                    height: 2.heightPercentage(context),
                  ),
                  Row(
                    mainAxisAlignment: MainAxisAlignment.end,
                    children: [
                      Expanded(
                        child: Container(
                          height: 2,
                          color: Colors.grey,
                        ),
                      ),
                      Padding(
                        padding: EdgeInsets.symmetric(
                          horizontal: 2.widthPercentage(context),
                        ),
                        child: Text(
                          'OR',
                          style: TextStyle(
                            fontSize: 15.sp(context),
                            fontFamily: Keys.Araboto,
                            fontWeight: FontWeight.bold,
                          ),
                        ),
                      ),
                      Expanded(
                        child: Container(
                          height: 2,
                          color: Colors.grey,
                        ),
                      )
                    ],
                  ),
                  SizedBox(
                    height: 2.heightPercentage(context),
                  ),
                  Center(
                    child: Text(
                      'Sign In with',
                      style: TextStyle(
                        fontSize: 15.sp(context),
                        fontFamily: Keys.Araboto,
                        fontWeight: FontWeight.bold,
                      ),
                    ),
                  ),
                  SizedBox(
                    height: 2.heightPercentage(context),
                  ),
                  RoundedButton(
                    title: 'Facebook',
                    buttoncolor: Color(0xff355ba9),
                    onPreesed: () {},
                    textcolor: Colors.white,
                  ),
                  SizedBox(
                    height: 2.heightPercentage(context),
                  ),
                  RoundedButton(
                    title: 'Google',
                    buttoncolor: Colors.grey.shade300,
                    onPreesed: () {},
                    textcolor: Colors.black,
                  ),
                ],
              ),
            ),
          ),
        ),
      ),
    );
  }
}
