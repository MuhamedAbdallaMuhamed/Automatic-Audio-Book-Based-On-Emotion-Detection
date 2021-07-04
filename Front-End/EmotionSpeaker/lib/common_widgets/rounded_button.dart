import 'package:flutter/material.dart';
import 'package:EmotionSpeaker/utils/sizing_extension.dart';

class RoundedButton extends StatelessWidget {
  RoundedButton(
      {@required this.title,
      @required this.buttoncolor,
      @required this.onPreesed,
      @required this.textcolor,
      this.bordercolor,
      this.fontSize});
  final Color buttoncolor;
  final Color textcolor;
  final String title;
  final Color bordercolor;
  final Function onPreesed;
  final double fontSize;
  @override
  Widget build(BuildContext context) {
    return Container(
      height: 40.0.hp(context),
      child: Material(
        shape: OutlineInputBorder(
          borderRadius: BorderRadius.circular(30.0),
          borderSide: BorderSide(color: bordercolor ?? buttoncolor, width: 1.0),
        ),
        color: buttoncolor,
        child: MaterialButton(
          onPressed: onPreesed,
          height: 40.0.hp(context),
          child: Text(
            title,
            style: TextStyle(
              fontFamily: 'Araboto',
              color: textcolor,
              fontSize: fontSize ?? 15.0.sp(context),
            ),
          ),
        ),
      ),
    );
  }
}
