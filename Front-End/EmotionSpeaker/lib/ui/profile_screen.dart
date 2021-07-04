import 'package:EmotionSpeaker/common_widgets/date_picker.dart';
import 'package:EmotionSpeaker/common_widgets/profile_picture.dart';
import 'package:EmotionSpeaker/common_widgets/text_input.dart';
import 'package:EmotionSpeaker/common_widgets/rounded_button.dart';
import 'package:EmotionSpeaker/constants/custom_colors.dart';
import 'package:EmotionSpeaker/constants/keys.dart';
import 'package:EmotionSpeaker/controller/user_controller.dart';
import 'package:EmotionSpeaker/models/result.dart';
import 'package:EmotionSpeaker/models/user.dart';
import 'package:EmotionSpeaker/ui/change_password_screen.dart';
import 'package:EmotionSpeaker/ui/home_screen.dart';
import 'package:flutter/material.dart';
import 'package:EmotionSpeaker/utils/sizing_extension.dart';
import 'package:get/get.dart';
import 'package:EmotionSpeaker/common_widgets/phone_number_input.dart';
import 'package:EmotionSpeaker/common_widgets/gender_input.dart';
import 'package:modal_progress_hud/modal_progress_hud.dart';

String gender;
String counrtyCode = '+20';
String phoneNumber;
String birthdayDate;
bool edit = false;
enum Selection { updateData, updatePassword }

class ProfileScreen extends StatefulWidget {
  final bool notRegister;

  const ProfileScreen({
    Key key,
    this.notRegister = false,
  }) : super(key: key);
  @override
  _ProfileScreenState createState() => _ProfileScreenState();
}

class _ProfileScreenState extends State<ProfileScreen> {
  final userController = Get.find<UserController>();

  final GlobalKey<FormState> _formKey = GlobalKey<FormState>();

  final TextEditingController firstName = TextEditingController();

  final TextEditingController lastName = TextEditingController();

  final TextEditingController email = TextEditingController();

  final TextEditingController password = TextEditingController();

  final TextEditingController confirmPassword = TextEditingController();

  final TextEditingController phone = TextEditingController();

  final TextEditingController birthDate = TextEditingController();
  bool loading = false;
  @override
  void initState() {
    super.initState();
    gender = 'Male';
    phoneNumber = null;
    if (widget.notRegister) {
      User user = Get.find<UserController>().mainUser;
      firstName.text = user.first_name;
      lastName.text = user.last_name;
      phone.text = user.phoneWithoutCode;
      counrtyCode = user.countryCode;
      birthDate.text = user.birthday;
      email.text = user.email;
      gender = user.gender;
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: CustomColors.backgroundColor,
      appBar: AppBar(
        backgroundColor: CustomColors.color1,
        centerTitle: true,
        title: Text(
          !widget.notRegister ? 'Register' : 'Profile',
          style: TextStyle(
            fontFamily: Keys.Araboto,
          ),
        ),
        actions: [
          if (widget.notRegister && !edit)
            PopupMenuButton(
              icon: Icon(
                Icons.more_vert,
                size: 30.sp(context),
              ),
              onSelected: (value) async {
                if (value == Selection.updateData) {
                  setState(() {
                    edit = !edit;
                  });
                } else if (value == Selection.updatePassword) {
                  Get.to(ChangePasswordScreen());
                }
              },
              itemBuilder: (context) => <PopupMenuEntry>[
                PopupMenuItem(
                  value: Selection.updateData,
                  child: Text(
                    'Edit',
                    style: TextStyle(
                      fontFamily: 'Araboto',
                      fontSize: 18.sp(context),
                    ),
                  ),
                ),
                PopupMenuItem(
                  value: Selection.updatePassword,
                  child: Text(
                    'Change password',
                    style: TextStyle(
                      fontFamily: 'Araboto',
                      fontSize: 18.sp(context),
                    ),
                  ),
                ),
              ],
            ),
        ],
      ),
      body: ModalProgressHUD(
        inAsyncCall: loading,
        child: SafeArea(
          child: SingleChildScrollView(
            child: AbsorbPointer(
              absorbing: !edit && widget.notRegister,
              child: Form(
                key: _formKey,
                child: Padding(
                  padding: EdgeInsets.symmetric(
                    horizontal: 5.widthPercentage(context),
                  ),
                  child: Column(
                    crossAxisAlignment: CrossAxisAlignment.stretch,
                    children: [
                      SizedBox(
                        height: 2.heightPercentage(context),
                      ),
                      if (widget.notRegister)
                        ProfilePicture(
                          edit: !edit,
                          fileFun: (file) {},
                        ),
                      if (widget.notRegister)
                        SizedBox(
                          height: 2.heightPercentage(context),
                        ),
                      Text(
                        'First Name',
                        style: TextStyle(
                          fontSize: 18.sp(context),
                          fontFamily: Keys.Araboto,
                        ),
                      ),
                      TextInput(
                        validate: TextInput.validateText,
                        controller: firstName,
                      ),
                      SizedBox(
                        height: 1.heightPercentage(context),
                      ),
                      Text(
                        'Last Name',
                        style: TextStyle(
                          fontSize: 18.sp(context),
                          fontFamily: Keys.Araboto,
                        ),
                      ),
                      TextInput(
                        validate: TextInput.validateText,
                        controller: lastName,
                      ),
                      SizedBox(
                        height: 1.heightPercentage(context),
                      ),
                      Text(
                        'Phone',
                        style: TextStyle(
                          fontSize: 18.sp(context),
                          fontFamily: Keys.Araboto,
                        ),
                      ),
                      PhoneNumberInput(
                        phonecontroller: phone,
                        phoneNumber: phoneNumber,
                        codeFun: (code, code2) {
                          countryCode = code;
                        },
                        intialCode: countryCode,
                      ),
                      SizedBox(
                        height: 1.heightPercentage(context),
                      ),
                      Text(
                        'Email',
                        style: TextStyle(
                          fontSize: 18.sp(context),
                          fontFamily: Keys.Araboto,
                        ),
                      ),
                      TextInput(
                        validate: TextInput.validateText,
                        controller: email,
                      ),
                      SizedBox(
                        height: 1.heightPercentage(context),
                      ),
                      if (!widget.notRegister)
                        Text(
                          'Password',
                          style: TextStyle(
                            fontSize: 18.sp(context),
                            fontFamily: Keys.Araboto,
                          ),
                        ),
                      if (!widget.notRegister)
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
                      if (!widget.notRegister)
                        SizedBox(
                          height: 1.heightPercentage(context),
                        ),
                      if (!widget.notRegister)
                        Text(
                          'Confirm Password',
                          style: TextStyle(
                            fontSize: 18.sp(context),
                            fontFamily: Keys.Araboto,
                          ),
                        ),
                      if (!widget.notRegister)
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
                      if (widget.notRegister)
                        SizedBox(
                          height: 1.heightPercentage(context),
                        ),
                      Text(
                        'Birth Date',
                        style: TextStyle(
                          fontSize: 18.sp(context),
                          fontFamily: Keys.Araboto,
                        ),
                      ),
                      Stack(
                        children: [
                          TextInput(
                            validate: TextInput.validateText,
                            controller: birthDate,
                          ),
                          ShowCustomDatePicker(
                            controller: birthDate,
                            onChanged: (value) {
                              DateTime date = DateTime.parse(value);
                              birthdayDate = date.year.toString() +
                                  '-' +
                                  date.month.toString() +
                                  '-' +
                                  date.day.toString();
                              setState(() {
                                birthDate.text = birthdayDate;
                              });
                            },
                            startTime: birthdayDate ??
                                DateTime.now()
                                    .subtract(
                                      Duration(days: 10000),
                                    )
                                    .toIso8601String(),
                          ),
                        ],
                      ),
                      SizedBox(
                        height: 1.heightPercentage(context),
                      ),
                      if (widget.notRegister && !edit)
                        Text(
                          'Gender: $gender',
                          style: TextStyle(
                            fontSize: 18.sp(context),
                            fontFamily: Keys.Araboto,
                          ),
                        ),
                      if (!widget.notRegister || edit)
                        Text(
                          'Gender',
                          style: TextStyle(
                            fontSize: 18.sp(context),
                            fontFamily: Keys.Araboto,
                          ),
                        ),
                      if (!widget.notRegister || edit)
                        GenderInput(
                          gender: gender,
                          genderStr: (str) {
                            gender = str;
                          },
                        ),
                      SizedBox(
                        height: 3.heightPercentage(context),
                      ),
                    ],
                  ),
                ),
              ),
            ),
          ),
        ),
      ),
      bottomNavigationBar: !widget.notRegister
          ? Padding(
              padding: EdgeInsets.only(
                  bottom: 2.heightPercentage(context),
                  left: 2.widthPercentage(context),
                  right: 2.widthPercentage(context)),
              child: RoundedButton(
                title: 'Register',
                buttoncolor: CustomColors.color1,
                onPreesed: () async {
                  if (!_formKey.currentState.validate()) return;
                  setState(() {
                    loading = true;
                  });
                  print(counrtyCode);
                  String phoneN = phone.text[0] == '0'
                      ? phone.text.substring(1)
                      : phone.text;
                  User user = User(
                    email: email.text,
                    password: password.text,
                    birthday: birthdayDate,
                    first_name: firstName.text,
                    last_name: lastName.text,
                    gender: gender,
                    phone: counrtyCode + phoneN,
                    profile_image_url: null,
                  );
                  print(user);
                  Result result = await userController.userRegister(user: user);
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
            )
          : edit
              ? Padding(
                  padding: EdgeInsets.only(
                      bottom: 2.heightPercentage(context),
                      left: 2.widthPercentage(context),
                      right: 2.widthPercentage(context)),
                  child: RoundedButton(
                    title: 'Save',
                    buttoncolor: CustomColors.color1,
                    onPreesed: () async {
                      if (!_formKey.currentState.validate()) return;
                      setState(() {
                        loading = true;
                      });
                      print(counrtyCode);
                      String phoneN = phone.text[0] == '0'
                          ? phone.text.substring(1)
                          : phone.text;
                      User user = User(
                        email: email.text,
                        birthday: birthDate.text,
                        first_name: firstName.text,
                        last_name: lastName.text,
                        gender: gender,
                        phone: counrtyCode + phoneN,
                        profile_image_url: null,
                      );
                      print(user);
                      Result result =
                          await userController.userUpdate(user: user);
                      if (result is SuccessResult) {
                        setState(() {
                          edit = false;
                          FocusScope.of(context).requestFocus(new FocusNode());
                          loading = false;
                        });
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
                )
              : Container(
                  height: 0,
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
