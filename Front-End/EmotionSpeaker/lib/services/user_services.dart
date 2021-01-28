import 'package:EmotionSpeaker/api/dio_api.dart';
import 'package:EmotionSpeaker/constants/keys.dart';
import 'package:EmotionSpeaker/constants/user_base.dart';
import 'package:EmotionSpeaker/models/result.dart';
import 'package:EmotionSpeaker/models/user.dart';
import 'package:dio/dio.dart';
import 'dart:convert';

class UserServices {
  DioClient dio = DioClient();
  Future<Result> userLogin({User user}) async {
    try {
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
    } catch (e) {
      return Result.error('Application Error');
    }
  }

  Future<Result> userRegister({User user}) async {
    try {
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
    } catch (e) {
      return Result.error('Application Error');
    }
  }

  Future<Result> userUpdate({User user, String accessToken}) async {
    try {
      Map map = user.toMap();
      map.remove('email');
      Response response = await dio.put(
        uri: UserBase.Url + UserBase.Register,
        data: json.encode(map),
        options: Options(
          headers: {
            Keys.Authorization: Keys.Bearer + accessToken,
          },
        ),
      );
      if (response.statusCode == 201) {
        return Result.success(response.statusMessage);
      } else {
        String resultMessage = response.data['message'];
        return Result.error(resultMessage);
      }
    } catch (e) {
      return Result.error('Application Error');
    }
  }

  Future<Result> getUser({String accessToken}) async {
    try {
      Response response = await dio.get(
        uri: UserBase.Url + UserBase.Update,
        options: Options(
          headers: {
            Keys.Authorization: Keys.Bearer + accessToken,
          },
        ),
      );
      if (response.statusCode == 200) {
        print(response.data);
        print(User.fromMap(response.data));
        return Result.success(User.fromMap(response.data));
      } else {
        String resultMessage = response.data['message'];
        return Result.error(resultMessage);
      }
    } catch (e) {
      print(e);
      return Result.error('Application Error');
    }
  }

  Future<Result> userLogout({String accessToken}) async {
    try {
      Response response = await dio.delete(
        uri: UserBase.Url + UserBase.Logout,
        options: Options(
          headers: {
            Keys.Authorization: Keys.Bearer + accessToken,
          },
        ),
      );
      if (response.statusCode == 200) {
        return Result.success('success');
      } else {
        String resultMessage = response.data['message'];
        return Result.error(resultMessage);
      }
    } catch (e) {
      return Result.error('Application Error');
    }
  }

  Future<Result> updateToken({String refreshToken}) async {
    try {
      Response response = await dio.get(
        uri: UserBase.Url + UserBase.RefreshToken,
        options: Options(
          headers: {
            Keys.Authorization: Keys.Bearer + refreshToken,
          },
        ),
      );
      if (response.statusCode == 200) {
        print(response.data);
        print(User.fromMap(response.data));
        return Result.success(User.fromMap(response.data));
      } else {
        String resultMessage = response.data['message'];
        return Result.error(resultMessage);
      }
    } catch (e) {
      print(e);
      return Result.error('Application Error');
    }
  }
}
