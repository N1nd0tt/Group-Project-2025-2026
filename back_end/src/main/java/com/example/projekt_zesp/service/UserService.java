package com.example.projekt_zesp.service;

import com.example.projekt_zesp.dto.UserProfileDto;

public interface UserService {
    UserProfileDto getUserProfile(String userId);
}
