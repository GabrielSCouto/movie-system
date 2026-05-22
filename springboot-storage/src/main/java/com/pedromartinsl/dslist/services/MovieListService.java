package com.pedromartinsl.dslist.services;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import com.pedromartinsl.dslist.dto.MovieListDTO;
import com.pedromartinsl.dslist.entities.MovieList;
import com.pedromartinsl.dslist.projections.MovieMinProjection;
import com.pedromartinsl.dslist.repositories.MovieListRepository;
import com.pedromartinsl.dslist.repositories.MovieRepository;


@Service
public class MovieListService {
	
	@Autowired
	private MovieListRepository movieListRepository;

	@Autowired
	private MovieRepository movieRepository;
	
	@Transactional(readOnly = true)
	public List<MovieListDTO> findAll() {
		List<MovieList> result = movieListRepository.findAll();
		return result.stream().map(MovieListDTO::new).toList();
	}

	@Transactional
	public void move(Long listId, int sourceIndex, int destinationIndex) {
		List<MovieMinProjection> list = movieRepository.searchByList(listId);
		MovieMinProjection obj = list.remove(sourceIndex);
		list.add(destinationIndex, obj);
		int min = sourceIndex < destinationIndex ? sourceIndex : destinationIndex;
		int max = sourceIndex < destinationIndex ? destinationIndex : sourceIndex;
		for (int i = min; i <= max; i++) {
			movieListRepository.updateBelongingPosition(listId, list.get(i).getId(), i);
		}
	}
}