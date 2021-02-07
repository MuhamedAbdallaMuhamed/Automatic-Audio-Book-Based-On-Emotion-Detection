import 'package:EmotionSpeaker/models/user.dart';
import 'package:EmotionSpeaker/services/user_services.dart';
import 'package:EmotionSpeaker/models/result.dart';

class UserRepository {
  UserServices userServices = UserServices();
  Future<Result> userLogin({User user}) async {
    try {
      Result result = await userServices.userLogin(user: user);
      return result;
    } catch (e) {
      return Result.error('Application Error');
    }
  }

  Future<Result> userRegister({User user}) async {
    try {
      Result result = await userServices.userRegister(user: user);
      return result;
    } catch (e) {
      return Result.error('Application Error');
    }
  }

  Future<Result> getUser({String accessToken}) async {
    try {
      Result result = await userServices.getUser(accessToken: accessToken);
      return result;
    } catch (e) {
      return Result.error('Application Error');
    }
  }

  Future<Result> getResetPasswordCode({String email}) async {
    try {
      Result result = await userServices.getResetPasswordCode(email: email);
      return result;
    } catch (e) {
      return Result.error('Application Error');
    }
  }

  Future<Result> resetPasswordCode(
      {String email, String code, String password}) async {
    try {
      Result result = await userServices.resetPassword(
        email: email,
        code: code,
        password: password,
      );
      return result;
    } catch (e) {
      return Result.error('Application Error');
    }
  }

  Future<Result> userUpdate({User user, String accessToken}) async {
    try {
      Result result =
          await userServices.userUpdate(user: user, accessToken: accessToken);
      return result;
    } catch (e) {
      return Result.error('Application Error');
    }
  }

  Future<Result> userLogut({String accessToken}) async {
    try {
      Result result = await userServices.userLogout(accessToken: accessToken);
      return result;
    } catch (e) {
      return Result.error('Application Error');
    }
  }
}
