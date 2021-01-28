import 'dart:convert';

class User {
  String email;
  // ignore: non_constant_identifier_names
  String first_name;
  // ignore: non_constant_identifier_names
  String last_name;
  String gender;
  String phone;
  String birthDay;
  String password;
  User({
    this.email,
    this.first_name,
    this.last_name,
    this.gender,
    this.phone,
    this.birthDay,
    this.password,
  });

  User copyWith({
    String email,
    String first_name,
    String last_name,
    String gender,
    String phone,
    String birthDay,
    String password,
  }) {
    return User(
      email: email ?? this.email,
      first_name: first_name ?? this.first_name,
      last_name: last_name ?? this.last_name,
      gender: gender ?? this.gender,
      phone: phone ?? this.phone,
      birthDay: birthDay ?? this.birthDay,
      password: password ?? this.password,
    );
  }

  Map<String, dynamic> toMap() {
    return {
      'email': email,
      'first_name': first_name,
      'last_name': last_name,
      'gender': gender,
      'phone': phone,
      'birthDay': birthDay,
      'password': password,
    };
  }

  factory User.fromMap(Map<String, dynamic> map) {
    if (map == null) return null;

    return User(
      email: map['email'],
      first_name: map['first_name'],
      last_name: map['last_name'],
      gender: map['gender'],
      phone: map['phone'],
      birthDay: map['birthDay'],
      password: map['password'],
    );
  }

  String toJson() => json.encode(toMap());

  factory User.fromJson(String source) => User.fromMap(json.decode(source));

  @override
  String toString() {
    return 'User(email: $email, first_name: $first_name, last_name: $last_name, gender: $gender, phone: $phone, birthDay: $birthDay, password: $password)';
  }

  @override
  bool operator ==(Object o) {
    if (identical(this, o)) return true;

    return o is User &&
        o.email == email &&
        o.first_name == first_name &&
        o.last_name == last_name &&
        o.gender == gender &&
        o.phone == phone &&
        o.birthDay == birthDay &&
        o.password == password;
  }

  @override
  int get hashCode {
    return email.hashCode ^
        first_name.hashCode ^
        last_name.hashCode ^
        gender.hashCode ^
        phone.hashCode ^
        birthDay.hashCode ^
        password.hashCode;
  }
}
