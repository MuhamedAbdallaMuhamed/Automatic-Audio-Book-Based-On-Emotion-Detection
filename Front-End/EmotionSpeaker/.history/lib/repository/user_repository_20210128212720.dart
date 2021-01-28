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
          headers: {
            Keys.Authorization: Keys.Bearer + accessToken,
          },
  Future<Result> userLogut({String accessToken}) async {
    try {
      Result result = await userServices.userLogout(accessToken: accessToken);
      return result;
    } catch (e) {
      return Result.error('Application Error');
    }
  }
}
