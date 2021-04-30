import 'package:EmotionSpeaker/constants/custom_colors.dart';
import 'package:EmotionSpeaker/controller/user_controller.dart';
import 'package:EmotionSpeaker/ui/pick_book_screen.dart';
import 'package:EmotionSpeaker/ui/register_or_login_screen.dart';
import 'package:flutter/material.dart';
import 'package:EmotionSpeaker/constants/Keys.dart';
import 'package:EmotionSpeaker/utils/sizing_extension.dart';
import 'package:get/get.dart';
import 'package:hidden_drawer_menu/controllers/simple_hidden_drawer_controller.dart';
import 'package:hidden_drawer_menu/simple_hidden_drawer/simple_hidden_drawer.dart';
import 'package:EmotionSpeaker/ui/profile_screen.dart';

class HomeScreen extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return SimpleHiddenDrawer(
      menu: Menu(),
      contentCornerRadius: 25.0,
      slidePercent: 60.0,
      verticalScalePercent: 80.0,
      screenSelectedBuilder: (position, controller) {
        return Scaffold(
          backgroundColor: CustomColors.backgroundColor,
          appBar: AppBar(
            automaticallyImplyLeading: false,
            backgroundColor: CustomColors.color1,
            centerTitle: true,
            leading: IconButton(
              icon: Icon(
                Icons.menu_outlined,
                size: 30.sp(context),
              ),
              onPressed: () {
                controller.open();
              },
            ),
            title: Text(
              'Book Beat',
              style: TextStyle(
                fontFamily: Keys.Araboto,
                fontWeight: FontWeight.bold,
                letterSpacing: 0.8,
              ),
            ),
          ),
          floatingActionButton: FloatingActionButton(
            onPressed: () {
              Get.to(
                PickBookScreen(),
              );
            },
            child: Icon(
              Icons.add,
              size: 30,
            ),
            backgroundColor: CustomColors.color1,
          ),
        );
      },
    );
  }
}

class Menu extends StatelessWidget {
  Menu({
    Key key,
  }) : super(key: key);
  final userController = Get.find<UserController>();

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.white,
      body: SafeArea(
        child: Padding(
          padding: EdgeInsets.symmetric(
            horizontal: 2.widthPercentage(context),
          ),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.stretch,
            children: [
              SizedBox(
                height: 4.heightPercentage(context),
              ),
              MenuItem(
                ontap: () {
                  SimpleHiddenDrawerController.of(context).toggle();
                },
                text: 'Requests',
              ),
              SizedBox(
                height: 1.heightPercentage(context),
              ),
              MenuItem(
                ontap: () {
                  SimpleHiddenDrawerController.of(context).toggle();
                },
                text: 'Books',
              ),
              SizedBox(
                height: 1.heightPercentage(context),
              ),
              MenuItem(
                ontap: () {
                  SimpleHiddenDrawerController.of(context).toggle();
                  Get.to(ProfileScreen(
                    notRegister: true,
                  ));
                },
                text: 'Profile',
              ),
              SizedBox(
                height: 1.heightPercentage(context),
              ),
              MenuItem(
                ontap: () {
                  SimpleHiddenDrawerController.of(context).toggle();
                  userController.userLogut();
                  Get.offAll(RegisterOrLoginScreen());
                },
                text: 'Logout',
              ),
            ],
          ),
        ),
      ),
    );
  }
}

class MenuItem extends StatelessWidget {
  const MenuItem({
    Key key,
    @required this.ontap,
    @required this.text,
  }) : super(key: key);
  final Function ontap;
  final String text;
  @override
  Widget build(BuildContext context) {
    return GestureDetector(
      onTap: ontap,
      child: Text(
        text,
        style: TextStyle(
          color: CustomColors.color1,
          fontSize: 18.sp(context),
          fontFamily: Keys.Araboto,
          fontWeight: FontWeight.bold,
        ),
      ),
    );
  }
}
