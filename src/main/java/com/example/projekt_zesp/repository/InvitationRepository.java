package com.example.projekt_zesp.repository;

import com.example.projekt_zesp.models.Invitation;
import org.springframework.data.jpa.repository.JpaRepository;

import java.util.List;

public interface InvitationRepository extends JpaRepository<Invitation, Long> {
    List<Invitation> findByReceiverId(String receiverId);
    List<Invitation> findBySenderId(String senderId);
}
