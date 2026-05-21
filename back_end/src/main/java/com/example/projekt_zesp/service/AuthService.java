package com.example.projekt_zesp.service;

import com.example.projekt_zesp.models.User;

public interface AuthService {
    void register(String login, String rawPassword);
    User findByLogin(String login);
}
