import 'package:flutter/material.dart';
import 'package:EmotionSpeaker/constants/custom_colors.dart';
import 'package:EmotionSpeaker/utils/sizing_extension.dart';
import 'package:EmotionSpeaker/common_widgets/text_input.dart';
import 'package:country_code_picker/country_code_picker.dart';
import 'package:mask_text_input_formatter/mask_text_input_formatter.dart';

String countryCode = '+20';

class PhoneNumberInput extends StatelessWidget {
  PhoneNumberInput({
    this.phoneNumber,
    this.phonecontroller,
    this.codeFun,
    this.intialCode,
  });

  final TextEditingController phonecontroller;
  final String phoneNumber;
  final Function(String value, String isoCode) codeFun;
  final String intialCode;
  @override
  Widget build(BuildContext context) {
    return Row(
      textDirection: TextDirection.ltr,
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        Expanded(
          flex: 1,
          child: CountryCodePicker(
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
                //width: 65.0.wp(context),
                height: 6.heightPercentage(context),
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
                        crossAxisAlignment: CrossAxisAlignment.center,
                        children: [
                          Text(
                            countrycode.dialCode,
                            textDirection: TextDirection.ltr,
                          ),
                          SizedBox(
                            width: 0.75,
                          ),
                          ClipRRect(
                            borderRadius: BorderRadius.circular(180),
                            child: Image.asset(
                              countrycode.flagUri,
                              package: 'country_code_picker',
                              width: 25.0.wp(context),
                              height: 50.0.wp(context),
                            ),
                          ),
                        ],
                      ),
                    ),
                  ],
                ),
              );
            },
            initialSelection: this.intialCode ?? '+20',
            favorite: ['+20'],
            showCountryOnly: false,
            showFlagMain: true,
            alignLeft: true,
            hideMainText: true,
            onChanged: (CountryCode code) {
              countryCode = code.dialCode;
              codeFun(countryCode, code.code);
            },
          ),
        ),
        SizedBox(
          width: 5,
        ),
        Expanded(
          flex: 3,
          child: TextInput(
            textDirection: TextDirection.ltr,
            controller: phonecontroller,
            broderRadius: 9,
            inputType: TextInputType.phone,
            bordercolor: CustomColors.color1,
            validate: TextInput.validatePhone,
            formatter: [
              MaskTextInputFormatter(
                mask: "",
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
