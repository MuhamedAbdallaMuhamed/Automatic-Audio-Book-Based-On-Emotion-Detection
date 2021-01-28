import 'package:EmotionSpeaker/common_widgets/hidden_menu/simple_hidden_drawer/simple_hidden_drawer.dart';
import 'package:EmotionSpeaker/constants/custom_colors.dart';
import 'package:flutter/material.dart';
import 'package:EmotionSpeaker/constants/Keys.dart';
import 'package:EmotionSpeaker/utils/sizing_extension.dart';

class HomeScreen extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return SimpleHiddenDrawer(
      menu: Menu(),
      contentCornerRadius: 25.0,
      slidePercent: 60.0,
      enableRotateAnimation: true,
      verticalScalePercent: 80.0,
      screenSelectedBuilder: (position, controller) {
        return Scaffold(
          backgroundColor: CustomColors.backgroundColor,
          appBar: AppBar(
            automaticallyImplyLeading: false,
            backgroundColor: Colors.blue,
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
        );
      },
    );
  }
}

class Menu extends StatelessWidget {
  const Menu({
    Key key,
  }) : super(key: key);

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
                ontap: () {},
                text: 'Requests',
              ),
              SizedBox(
                height: 1.heightPercentage(context),
              ),
              MenuItem(
                ontap: () {},
                text: 'Books',
              ),
              SizedBox(
                height: 1.heightPercentage(context),
              ),
              MenuItem(
                ontap: () {},
                text: 'Profile',
              ),
              SizedBox(
                height: 1.heightPercentage(context),
              ),
              MenuItem(
                ontap: () {},
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
          color: Colors.black,
          fontSize: 18.sp(context),
          fontFamily: Keys.Araboto,
          fontWeight: FontWeight.bold,
        ),
      ),
    );
  }
}
