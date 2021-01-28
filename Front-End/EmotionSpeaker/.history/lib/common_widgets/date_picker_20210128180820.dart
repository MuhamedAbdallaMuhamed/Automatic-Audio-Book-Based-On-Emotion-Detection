import 'package:EmotionSpeaker/common_widgets/text_input.dart';
import 'package:flutter/material.dart';
import 'package:EmotionSpeaker/constants/custom_colors.dart';
import 'package:EmotionSpeaker/utils/sizing_extension.dart';
import 'package:datetime_picker_formfield/datetime_picker_formfield.dart';
import 'package:get/get.dart';
import 'package:intl/intl.dart';
import 'package:Enaba/constants/keys.dart';

class ShowCustomDatePicker extends StatelessWidget {
  ShowCustomDatePicker(
      {@required this.onChanged,
      this.borderColor = EnabaColors.yellowBrown,
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
      format: DateFormat('EEEE، d MMM yyyy', Get.locale.languageCode),
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
        focusColor: EnabaColors.yellowBrown,
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

class ShowHejriCustomDatePicker extends StatelessWidget {
  ShowHejriCustomDatePicker({
    @required this.onChanged,
    this.borderColor = EnabaColors.yellowBrown,
    @required this.startTime,
    this.controller,
  });
  final Function(HijriCalendar date) onChanged;
  final Color borderColor;
  final HijriCalendar startTime;
  final TextEditingController controller;
  @override
  Widget build(BuildContext context) {
    return Container(
      child: GestureDetector(
        onTap: () async {
          final HijriCalendar picked = await showHijriDatePicker(
            context: context,
            initialDate: startTime,
            firstDate: HijriCalendar.fromDate(DateTime.now().subtract(Duration(
              days: 21900,
            ))),
            lastDate: HijriCalendar.fromDate(
                DateTime.now().subtract(Duration(days: 7665))),
            initialDatePickerMode: DatePickerMode.day,
          );
          HijriCalendar.setLocal(Get.locale.languageCode);
          controller.text = picked.toFormat('dd MMMM yyyy').toString();
          onChanged(picked);
        },
        child: Stack(
          children: [
            TextInput(
              controller: controller,
              validate: TextInput.validateText,
            ),
            TextInput(
              //  style: TextStyle(fontFamily: 'Araboto'),
              bordercolor: borderColor,
              controller: controller,
              enabled: false,
              hint: '--/--/-------',
              textIcon: Icon(
                Icons.date_range,
                color: Colors.black,
              ),

              //  cursorColor: EnabaColors.yellowBrown,
              // decoration: InputDecoration(
              //   hintText: '--/--/-------',
              //   focusColor: EnabaColors.yellowBrown,
              //   suffixIcon: Icon(
              //     Icons.date_range,
              //     color: Colors.black,
              //   ),
              //   fillColor: Colors.white,
              //   filled: true,
              //   contentPadding: EdgeInsets.symmetric(
              //     horizontal: 2.0.widthPercentage(context),
              //   ),
              //   focusedBorder: OutlineInputBorder(
              //     borderSide: BorderSide(
              //       color: borderColor,
              //       width: 2.0,
              //     ),
              //     borderRadius: BorderRadius.all(Radius.circular(5.0)),
              //   ),
              //   enabledBorder: OutlineInputBorder(
              //     borderSide: BorderSide(color: borderColor, width: 1.0),
              //     borderRadius: BorderRadius.all(Radius.circular(5.0)),
              //   ),
              //   border: OutlineInputBorder(
              //     borderSide: BorderSide(
              //       color: borderColor,
              //       width: 2.0,
              //     ),
              //     borderRadius: BorderRadius.all(Radius.circular(5.0)),
              //   ),
              // ),
              // // type: DateTimePickerType.date,
              // dateMask: 'd ,MMM, yyyy',
              // initialValue: startTime.toString(),
              // firstDate: DateTime(1900),
              // lastDate: DateTime(2100),
              // dateLabelText: 'Date',
            ),
          ],
        ),
      ),
    );
  }
}
