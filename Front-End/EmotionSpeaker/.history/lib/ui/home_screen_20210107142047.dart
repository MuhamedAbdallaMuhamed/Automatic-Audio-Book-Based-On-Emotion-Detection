import 'package:EmotionSpeaker/common_widgets/hidden_menu/controllers/simple_hidden_drawer_controller.dart';
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
              'Emotion Speaker',
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
            children: [
              SizedBox(
                height: 4.heightPercentage(context),
              ),
              Text(
                'My Books',
                style: TextStyle(
                  color: CustomColors.color2,
                  fontSize: 18.sp(context),
                  fontFamily: Keys.Araboto,
                  fontWeight: FontWeight.bold,
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }
}
