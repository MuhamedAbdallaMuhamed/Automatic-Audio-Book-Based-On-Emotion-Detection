import 'package:EmotionSpeaker/constants/keys.dart';
import 'package:EmotionSpeaker/constants/shared_preferences_keys.dart';
import 'package:EmotionSpeaker/models/user.dart';
import 'package:EmotionSpeaker/utils/shared_pref.dart';
import 'package:get/state_manager.dart';
import 'package:EmotionSpeaker/repository/user_repository.dart';
import 'package:EmotionSpeaker/models/result.dart';
import 'package:intl_phone_number_input/intl_phone_number_input.dart';

class UserController extends GetxController {
  UserRepository userRepository = UserRepository();
  User mainUser;
  Future<Result> openApp() async {
    await SharedPref.initialize();
    bool login = SharedPref.pref.getBool(SharedPreferencesKeys.Login) ?? false;
    if (login) {
      String email = SharedPref.pref.getString(SharedPreferencesKeys.Email);
      String password =
          SharedPref.pref.getString(SharedPreferencesKeys.Password);
      mainUser = User(
        email: email,
        password: password,
      );
      return await userLogin(user: mainUser);
    } else
      return Result.error(Keys.Logout);
  }

  Future<Result> userLogin({User user}) async {
    try {
      Result result = await userRepository.userLogin(user: user);
      if (result is SuccessResult) {
        mainUser = user;
        mainUser = result.getSuccessData();
        mainUser.password = user.password;
        await _setPhoneNumber();
        SharedPref.pref.setBool(SharedPreferencesKeys.Login, true);
        SharedPref.pref.setString(SharedPreferencesKeys.Email, user.email);
        SharedPref.pref
            .setString(SharedPreferencesKeys.Password, user.password);
        return Result.success('Success');
      } else
        return result;
    } catch (e) {
      return Result.error('Application Error');
    }
  }

  Future<Result> userRegister({User user}) async {
    try {
      Result result = await userRepository.userRegister(user: user);
      if (result is SuccessResult) {
        mainUser = result.getSuccessData();
        await _setPhoneNumber();
        SharedPref.pref.setBool(SharedPreferencesKeys.Login, true);
        SharedPref.pref.setString(SharedPreferencesKeys.Email, user.email);
        SharedPref.pref
            .setString(SharedPreferencesKeys.Password, user.password);
        return Result.success('Success');
      } else
        return result;
    } catch (e) {
      return Result.error('Application Error');
    }
  }

  Future<Result> getResetPasswordCode({String email}) async {
    try {
      Result result = await userRepository.getResetPasswordCode(email: email);
      if (result is SuccessResult) {
        return Result.success('Success');
      } else
        return result;
    } catch (e) {
      return Result.error('Application Error');
    }
  }

  Future<Result> resetPassword(
      {String email, String code, String password}) async {
    try {
      Result result = await userRepository.resetPasswordCode(
        email: email,
        code: code,
        password: password,
      );
      if (result is SuccessResult) {
        return Result.success('Success');
      } else
        return result;
    } catch (e) {
      return Result.error('Application Error');
    }
  }

  Future<Result> getUser({User user}) async {
    try {
      Result result =
          await userRepository.getUser(accessToken: mainUser.access_token);
      if (result is SuccessResult) {
        User newUser = result.getSuccessData();
        newUser.password = mainUser.password;
        mainUser = newUser;
        await _setPhoneNumber();
        return Result.success('Success');
      } else
        return result;
    } catch (e) {
      return Result.error('Application Error');
    }
  }

  Future<Result> userUpdate({User user}) async {
    try {
      Result result = await userRepository.userUpdate(
        user: user,
        accessToken: mainUser.access_token,
      );
      if (result is SuccessResult) {
        user.password = mainUser.password;
        user.access_token = mainUser.access_token;
        user.refresh_token = mainUser.refresh_token;
        mainUser = user;
        await _setPhoneNumber();
        return Result.success('Success');
      } else
        return result;
    } catch (e) {
      return Result.error('Application Error');
    }
  }

  Future<Result> updatePassword({User user, String oldPassword}) async {
    try {
      if (oldPassword != mainUser.password)
        return Result.error('old password not correct');
      Result result = await userRepository.userUpdate(
        user: user,
        accessToken: mainUser.access_token,
      );
      if (result is SuccessResult) {
        mainUser.password = user.password;
        SharedPref.pref
            .setString(SharedPreferencesKeys.Password, user.password);
        return Result.success('Success');
      } else
        return result;
    } catch (e) {
      return Result.error('Application Error');
    }
  }

  void userLogut() {
    mainUser = null;
    SharedPref.pref.setBool(SharedPreferencesKeys.Login, false);
    SharedPref.pref.setString(SharedPreferencesKeys.Email, '');
    SharedPref.pref.setString(SharedPreferencesKeys.Password, '');
  }

  Future<void> _setPhoneNumber() async {
    try {
      PhoneNumber number =
          await PhoneNumber.getRegionInfoFromPhoneNumber(mainUser.phone);
      String parsableNumber = number.parseNumber();
      mainUser.countryCode = '+' + number.dialCode;
      String phonenumber = parsableNumber.replaceAll('+', '');
      mainUser.phoneWithoutCode = phonenumber;
      print(mainUser.countryCode);
      print(mainUser.phoneWithoutCode);
    } catch (e) {
      print(e);
    }
  }
}
