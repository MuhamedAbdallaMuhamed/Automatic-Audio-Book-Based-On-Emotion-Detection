import 'package:EmotionSpeaker/repository/audio_order_repository.dart';
import 'package:get/state_manager.dart';
import 'package:EmotionSpeaker/models/result.dart';
import 'package:EmotionSpeaker/models/audio_order.dart';

class AudioOrderController extends GetxController {
  AudioOrderRepository audioOrderRepository = AudioOrderRepository();
  Future<Result> addAudioOrder(
      {AudioOrder audioOrder, String accessToken}) async {
    try {
      Result result = await audioOrderRepository.addAudioOrder(
        audioOrder: audioOrder,
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
}
