import 'package:dio/dio.dart';
import 'package:Enaba/constants/keys.dart';

class DioClient {
  static final Dio _dio = Dio();

  Future<dynamic> get({
    String uri,
    Map<String, dynamic> queryParameters,
    Options options,
    CancelToken cancelToken,
    ProgressCallback onReceiveProgress,
  }) async {
    try {
      final Response response = await _dio.get(
        uri,
        queryParameters: queryParameters,
        options: options,
        cancelToken: cancelToken,
        onReceiveProgress: onReceiveProgress,
      );
      return response;
    } catch (e) {
      if (e is DioError) {
        print(e.response);
        return e.response;
      }
      //  throw e;
    }
  }

  Future<dynamic> post({
    String uri,
    data,
    Map<String, dynamic> queryParameters,
    Options options,
    CancelToken cancelToken,
    ProgressCallback onSendProgress,
    ProgressCallback onReceiveProgress,
  }) async {
    try {
      final Response response = await _dio.post(
        uri,
        data: data,
        queryParameters: queryParameters,
        options: options,
        cancelToken: cancelToken,
        onSendProgress: onSendProgress,
        onReceiveProgress: onReceiveProgress,
      );
      return response;
    } catch (e) {
      if (e is DioError) {
        print(e.response);
      }
    }
  }

  Future<dynamic> put({
    String uri,
    data,
    Map<String, dynamic> queryParameters,
    Options options,
    CancelToken cancelToken,
    ProgressCallback onSendProgress,
    ProgressCallback onReceiveProgress,
  }) async {
    try {
      final Response response = await _dio.put(
        uri,
        data: data,
        queryParameters: queryParameters,
        options: options,
        cancelToken: cancelToken,
        onSendProgress: onSendProgress,
        onReceiveProgress: onReceiveProgress,
      );
      return response;
    } catch (e) {
      if (e is DioError) {
        print(e.response);
      }
    }
  }

  static Options getOptions({String userToken}) {
    return Options(
      headers: {
        Keys.Header_Authorization_Firebase: userToken,
        Keys.Header_X_Authorization_Firebase: userToken,
      },
    );
  }
}
