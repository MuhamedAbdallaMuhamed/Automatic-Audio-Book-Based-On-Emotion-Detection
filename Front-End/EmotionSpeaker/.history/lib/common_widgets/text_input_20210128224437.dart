import 'package:EmotionSpeaker/constants/custom_colors.dart';
import 'package:flutter/material.dart';
import 'package:EmotionSpeaker/utils/sizing_extension.dart';
import 'package:flutter/services.dart';
import 'package:get/get.dart';

class TextInput extends StatelessWidget {
  TextInput(
      {this.obscure = false,
      this.inputType = TextInputType.text,
      this.hint = '',
      this.textAlign = TextAlign.start,
      this.bordercolor = CustomColors.color1,
      this.controller,
      this.height,
      this.textColor = Colors.black,
      this.formatter,
      this.broderRadius = 5.0,
      this.textDirection,
      this.enabled = true,
      this.validate,
      this.textIcon,
      this.onChanged});
  final TextInputType inputType;
  final bool obscure;
  final String hint;
  final TextAlign textAlign;
  final Color bordercolor;
  final TextEditingController controller;
  final double height;
  final Color textColor;
  final List<TextInputFormatter> formatter;
  final double broderRadius;
  final TextDirection textDirection;
  final bool enabled;
  final Function validate;
  final Icon textIcon;
  final Function onChanged;
  @override
  Widget build(BuildContext context) {
    return Padding(
      padding: const EdgeInsets.symmetric(
        vertical: 0,
      ),
      child: Container(
        child: TextFormField(
          onChanged: onChanged,
          validator: validate ?? null,
          enabled: enabled,
          textDirection: textDirection,
          inputFormatters: formatter ?? [],
          controller: controller,
          obscureText: obscure,
          textAlign: textAlign,
          cursorHeight: 20.sp(context),
          style: TextStyle(
            fontFamily: 'Araboto',
            color: this.textColor,
            fontSize: 18.0.sp(context),
          ),
          keyboardType: inputType,
          decoration: InputDecoration(
            isDense: false,
            hintText: hint,
            fillColor: Colors.white,
            filled: true,
            contentPadding: EdgeInsets.symmetric(
              horizontal: 2.0.widthPercentage(context),
              vertical: 0,
            ),
            suffixIcon: textIcon ?? null,
            focusedBorder: OutlineInputBorder(
              borderSide: BorderSide(
                color: bordercolor,
                width: 2.0,
              ),
              borderRadius: BorderRadius.all(Radius.circular(broderRadius)),
            ),
            enabledBorder: OutlineInputBorder(
              borderSide: BorderSide(color: bordercolor, width: 1.0),
              borderRadius: BorderRadius.all(Radius.circular(broderRadius)),
            ),
            border: OutlineInputBorder(
              borderSide: BorderSide(
                color: bordercolor,
                width: 2.0,
              ),
              borderRadius: BorderRadius.all(
                Radius.circular(broderRadius),
              ),
            ),
          ),
        ),
      ),
    );
  }

  static String validateMail(String value) {
    if (value.isEmpty) {
      return 'Please enter the required information'.tr;
    }

    if (!RegExp(
            r"[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?")
        .hasMatch(value)) {
      return 'Please enter a valid email'.tr;
    }

    return null;
  }

  static String validateText(String value) {
    if (value.isEmpty) {
      return 'Please enter the required information'.tr;
    }
    return null;
  }

  static String validatePhone(String value) {
    {
      if (value.isEmpty) {
        return 'Please enter the required information'.tr;
      }
      return null;
    }
  }

  static String(String value1, String value2) {
    {
      if (value1.isEmpty) {
        return 'Please enter the required information'.tr;
      }
      if (value1 != value2) return "Password doesn't match";
      return null;
    }
  }
}
