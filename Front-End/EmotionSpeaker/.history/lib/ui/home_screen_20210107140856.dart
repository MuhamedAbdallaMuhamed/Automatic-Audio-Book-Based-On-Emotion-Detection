import 'package:EmotionSpeaker/common_widgets/hidden_menu/simple_hidden_drawer/simple_hidden_drawer.dart';
import 'package:EmotionSpeaker/constants/custom_colors.dart';
import 'package:flutter/material.dart';
import 'package:EmotionSpeaker/constants/Keys.dart';

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
            backgroundColor: CustomColors.color1,
            centerTitle: true,
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
      backgroundColor: CustomColors.color2,
      body: SafeArea(
        child: Column(
          children: [
            Text('Orders'),
          ],
        ),
      ),
    );
  }
}
