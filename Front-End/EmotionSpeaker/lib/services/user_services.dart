import 'dart:convert';

import 'package:EmotionSpeaker/api/dio_api.dart';
import 'package:EmotionSpeaker/constants/keys.dart';
import 'package:EmotionSpeaker/constants/user_base.dart';
import 'package:EmotionSpeaker/models/result.dart';
import 'package:EmotionSpeaker/models/user.dart';
import 'package:dio/dio.dart';

class UserServices {
  DioClient dio = DioClient();
  Future<Result> userLogin({User user}) async {
    Response response;
    try {
      response = await dio.post(
        uri: UserBase.Url + UserBase.Login,
        data: user.toJson(),
      );
      if (response.statusCode == 200) {
        return Result.success(User.fromMap(response.data));
      } else {
        print(response.statusCode);
        String resultMessage = response.data['message'];
        return Result.error(resultMessage);
      }
    } catch (e) {
      return Result.error(response.data['message']);
    }
  }

  Future<Result> userRegister({User user}) async {
    Response response;
    try {
      response = await dio.post(
        uri: UserBase.Url + UserBase.Register,
        data: user.toJson(),
      );
      if (response.statusCode == 201) {
        return Result.success(User.fromMap(response.data));
      } else {
        String resultMessage = response.data['message'];
        return Result.error(resultMessage);
      }
    } catch (e) {
      return Result.error(response.data['message']);
    }
  }

  Future<Result> userUpdate({User user, String accessToken}) async {
    try {
      Map map = user.toMap();
      map.remove('email');
      Response response = await dio.put(
        uri: UserBase.Url + UserBase.Update,
        data: json.encode(map),
        options: Options(
          headers: {
            Keys.Authorization: Keys.Bearer + accessToken,
          },
        ),
      );
      if (response.statusCode == 200) {
        return Result.success(response.statusMessage);
      } else {
        String resultMessage = response.data['message'];
        return Result.error(resultMessage);
      }
    } catch (e) {
      return Result.error('Application Error');
    }
  }

  Future<Result> getResetPasswordCode({String email}) async {
    try {
      print('send mail');
      Response response = await dio.get(
        uri: UserBase.Url + UserBase.ForgetPassword,
        queryParameters: {
          'email': email,
        },
      );
      print('response done ');
      if (response.statusCode == 200) {
        return Result.success(response.data['message']);
      } else {
        String resultMessage = response.data['message'];
        return Result.error(resultMessage);
      }
    } catch (e) {
      print(e);
      return Result.error('Application Error');
    }
  }

  Future<Result> resetPassword(
      {String email, String code, String password}) async {
    try {
      Response response = await dio.put(
        uri: UserBase.Url + UserBase.ForgetPassword,
        data: {
          'email': email,
          'password': password,
          "password_reset_code": code,
        },
      );
      if (response.statusCode == 200) {
        return Result.success(response.data['message']);
      } else {
        String resultMessage = response.data['message'];
        return Result.error(resultMessage);
      }
    } catch (e) {
      print(e);
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
