import 'package:EmotionSpeaker/api/dio_api.dart';
import 'package:EmotionSpeaker/constants/keys.dart';
import 'package:EmotionSpeaker/constants/user_base.dart';
import 'package:EmotionSpeaker/models/result.dart';
import 'package:EmotionSpeaker/models/user.dart';
import 'package:dio/dio.dart';

class UserServices {
  DioClient dio = DioClient();
  Future<Result> userLogin({User user}) async {
    Response response = await dio.post(
      uri: UserBase.Url + UserBase.Login,
      data: user.toJson(),
    );
    if (response.statusCode == 200) {
      String accessToken = response.data['access_token'];
      String refreshToken = response.data['refresh_token'];
      return Result.success([accessToken, refreshToken]);
    } else {
      String resultMessage = response.data['message'];
      return Result.error(resultMessage);
    }
  }

  Future<Result> userRegister({User user}) async {
    Response response = await dio.post(
      uri: UserBase.Url + UserBase.Register,
      data: user.toJson(),
    );
    if (response.statusCode == 201) {
      return Result.success(response.statusMessage);
    } else {
      String resultMessage = response.data['message'];
      return Result.error(resultMessage);
    }
  }

  Future<Result> userUpdate({User user}) async {
    Response response = await dio.put(
      uri: UserBase.Url + UserBase.Register,
      data: user.toJson(),
    );
    if (response.statusCode == 201) {
      return Result.success(response.statusMessage);
    } else {
      String resultMessage = response.data['message'];
      return Result.error(resultMessage);
    }
  }

  Future<Result> getUser({User user, String accessToken}) async {
    Response response = await dio.get(
      uri: UserBase.Url + UserBase.Update,
      options: Options(
        headers: {
          Keys.Authorization: Keys.Bearer + accessToken,
        },
      ),
    );
    if (response.statusCode == 200) {
      return Result.success(User.fromJson(response.data));
    } else {
      String resultMessage = response.data['message'];
      return Result.error(resultMessage);
    }
  }
}
