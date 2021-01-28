import 'package:EmotionSpeaker/constants/keys.dart';
import 'package:EmotionSpeaker/constants/shared_preferences_keys.dart';
import 'package:EmotionSpeaker/models/user.dart';
import 'package:EmotionSpeaker/utils/shared_pref.dart';
import 'package:get/state_manager.dart';

import 'package:EmotionSpeaker/repository/user_repository.dart';
import 'package:EmotionSpeaker/models/result.dart';

class UserController extends GetxController {
  String accessToken;
  String refreshToken;
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
        List list = result.getSuccessData();
        accessToken = list[0];
        refreshToken = list[1];
        SharedPref.pref.setBool(SharedPreferencesKeys.Login, true);
        SharedPref.pref.setString(SharedPreferencesKeys.Email, user.email);
        SharedPref.pref
            .setString(SharedPreferencesKeys.Password, user.password);
        Result result2 = await getUser();
        if (result2 is SuccessResult)
          return Result.success('Success');
        else
          return result2;
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
        return await userLogin(user: user);
      } else
        return result;
    } catch (e) {
      return Result.error('Application Error');
    }
  }

  Future<Result> getUser({User user}) async {
    try {
      Result result = await userRepository.getUser(accessToken: accessToken);
      if (result is SuccessResult) {
        User newUser = result.getSuccessData();
        newUser.password = mainUser.password;
        mainUser = newUser;
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
        accessToken: accessToken,
      );
      if (result is SuccessResult) {
        return Result.success('Success');
      } else
        return result;
    } catch (e) {
      return Result.error('Application Error');
    }
  }

  Future<Result> userLogut() async {
    try {
      Result result = await userRepository.userLogut(accessToken: accessToken);
      if (result is SuccessResult) {
        accessToken = null;
        refreshToken = null;
        SharedPref.pref.setBool(SharedPreferencesKeys.Login, false);
        SharedPref.pref.setString(SharedPreferencesKeys.Email, '');
        SharedPref.pref.setString(SharedPreferencesKeys.Password, '');
      }
      return result;
    } catch (e) {
      return Result.error('Application Error');
    }
  }
}
