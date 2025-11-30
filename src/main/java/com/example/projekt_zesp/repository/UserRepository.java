package com.example.projekt_zesp.repository;

import com.example.projekt_zesp.models.User;
import org.springframework.data.jpa.repository.JpaRepository;

public interface UserRepository extends JpaRepository<User, String> {
}
