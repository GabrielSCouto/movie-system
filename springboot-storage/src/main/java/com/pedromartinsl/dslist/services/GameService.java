package com.pedromartinsl.dslist.services;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;
import org.springframework.web.bind.annotation.PathVariable;

import com.pedromartinsl.dslist.dto.GameDTO;
import com.pedromartinsl.dslist.dto.GameMinDTO;
import com.pedromartinsl.dslist.entities.Game;
import com.pedromartinsl.dslist.projections.GameMinProjection;
import com.pedromartinsl.dslist.repositories.GameRepository;


@Service
public class GameService {
    
    @Autowired
	private GameRepository gameRepository;

	@Transactional(readOnly = true)
	public GameDTO findById(@PathVariable Long listId) {
		Game result = gameRepository.findById(listId).get();
		return new GameDTO(result);
	}
	
	public List<GameMinDTO> findAll() {
		List<Game> result = gameRepository.findAll();
		return result.stream().map(GameMinDTO::new).toList();
	}

	@Transactional(readOnly = true)
	public List<GameMinDTO> findByGameList(Long listId) {
		List<GameMinProjection> games = gameRepository.searchByList(listId);
		return games.stream().map(GameMinDTO::new).toList();
	}
	
}
