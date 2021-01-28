import 'package:EmotionSpeaker/common_widgets/text_input.dart';
import 'package:flutter/material.dart';
import 'package:EmotionSpeaker/constants/custom_colors.dart';
import 'package:EmotionSpeaker/utils/sizing_extension.dart';
import 'package:datetime_picker_formfield/datetime_picker_formfield.dart';
import 'package:get/get.dart';
import 'package:intl/intl.dart';
import 'package:EmotionSpeaker/constants/keys.dart';

class ShowCustomDatePicker extends StatelessWidget {
  ShowCustomDatePicker(
      {@required this.onChanged,
      this.borderColor = CustomColors.color1,
      @required this.startTime,
      this.controller});
  final Function(String date) onChanged;
  final Color borderColor;
  final String startTime;
  final TextEditingController controller;

  @override
  Widget build(BuildContext context) {
    return DateTimeField(
      controller: controller,
      validator: (value) => TextInput.validateText(value.toString()),
      format: DateFormat(
        'EEEE، d MMM yyyy',
      ),
      style: TextStyle(fontFamily: Keys.Araboto),
      onShowPicker: (context, currentValue) async {
        final date = await showDatePicker(
          context: context,
          helpText: '',
          firstDate: DateTime(1900),
          initialDate: currentValue ?? DateTime.now(),
          lastDate: DateTime(2100),
        );
        onChanged(date.toIso8601String());
        return date;
      },
      decoration: InputDecoration(
        focusColor: CustomColors.color1,
        suffixIcon: Icon(
          Icons.date_range,
          color: Colors.black,
        ),
        fillColor: Colors.white,
        filled: true,
        contentPadding: EdgeInsets.symmetric(
          horizontal: 2.0.widthPercentage(context),
        ),
        focusedBorder: OutlineInputBorder(
          borderSide: BorderSide(
            color: borderColor,
            width: 2.0,
          ),
          borderRadius: BorderRadius.all(Radius.circular(5.0)),
        ),
        enabledBorder: OutlineInputBorder(
          borderSide: BorderSide(color: borderColor, width: 1.0),
          borderRadius: BorderRadius.all(Radius.circular(5.0)),
        ),
        border: OutlineInputBorder(
          borderSide: BorderSide(
            color: borderColor,
            width: 2.0,
          ),
          borderRadius: BorderRadius.all(Radius.circular(5.0)),
        ),
      ),
    );
  }
}
