import 'package:EmotionSpeaker/common_widgets/text_input.dart';
import 'package:flutter/material.dart';
import 'package:EmotionSpeaker/constants/custom_colors.dart';
import 'package:EmotionSpeaker/utils/sizing_extension.dart';
import 'package:country_code_picker/country_code_picker.dart';
import 'package:mask_text_input_formatter/mask_text_input_formatter.dart';

String countryCode = '+20';

class PhoneNumberInput extends StatelessWidget {
  PhoneNumberInput({
    this.phoneNumber,
    this.phonecontroller,
  });

  final TextEditingController phonecontroller;
  final String phoneNumber;

  @override
  Widget build(BuildContext context) {
    return Row(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        CountryCodePicker(
          builder: (countrycode) {
            return Container(
              decoration: BoxDecoration(
                border: Border.all(
                  color: CustomColors.color1,
                ),
                borderRadius: BorderRadius.circular(
                  9.0,
                ),
                color: Colors.white,
              ),
              width: 60.0.wp(context),
//              height: 6.heightPercentage(context),
              child: Stack(
                children: [
                  TextInput(
                    enabled: false,
                  ),
                  Positioned(
                    bottom: 0.8.heightPercentage(context),
                    top: 0.8.heightPercentage(context),
                    left: .5.widthPercentage(context),
                    right: .5.widthPercentage(context),
                    child: Row(
                      mainAxisAlignment: MainAxisAlignment.center,
                      crossAxisAlignment: CrossAxisAlignment.stretch,
                      children: [
                        ClipRRect(
                          borderRadius: BorderRadius.circular(180),
                          child: Image.asset(
                            countrycode.flagUri,
                            package: 'country_code_picker',
                            width: 30.0.wp(context),
//                                height: 25.0.wp(context),
                          ),
                        ),
                        Icon(
                          Icons.arrow_drop_down,
                          size: 20.0.sp(context),
                        ),
                      ],
                    ),
                  ),
                ],
              ),
            );
          },
          initialSelection: '+20',
          favorite: ['+20'],
          showCountryOnly: true,
          showFlagMain: true,
          alignLeft: true,
          hideMainText: true,
          onChanged: (CountryCode code) {
            countryCode = code.dialCode;
          },
        ),
        SizedBox(
          width: 5.0.wp(context),
        ),
        Expanded(
          child: TextInput(
            textDirection: TextDirection.ltr,
            controller: phonecontroller,
            broderRadius: 9,
            inputType: TextInputType.phone,
            bordercolor: CustomColors.color1,
            validate: TextInput.validatePhone,
            formatter: [
              MaskTextInputFormatter(
                filter: {
                  "#": RegExp(r'[0-9]'),
                },
              ),
            ],
          ),
        ),
      ],
    );
  }
}
