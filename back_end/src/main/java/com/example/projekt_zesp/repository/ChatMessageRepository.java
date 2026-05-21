package com.example.projekt_zesp.repository;

import com.example.projekt_zesp.models.ChatMessage;
import org.springframework.data.jpa.repository.JpaRepository;

import java.util.List;

public interface ChatMessageRepository extends JpaRepository<ChatMessage, Long> {
    List<ChatMessage> findByCampaignIdOrderByCreatedAtAsc(String campaignId);
}
