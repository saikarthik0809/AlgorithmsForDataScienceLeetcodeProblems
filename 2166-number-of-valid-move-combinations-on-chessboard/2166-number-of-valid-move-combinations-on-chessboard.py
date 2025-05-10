class Solution:
    def countCombinations(self, pieces: List[str], positions: List[List[int]]) -> int:
        
        moves = { "rook" : [ (1,0),(-1,0),(0,-1),(0,1) ],
                  "bishop" : [ (1,1),(-1,-1),(1,-1),(-1,1) ],
                  "queen" : [ (1,0),(-1,0),(0,-1),(0,1),(1,1),(-1,-1),(1,-1),(-1,1) ] }

        # bq -> blocked cells where we can't be. ( i, j, time ) as we care about time too
        # nbq -> same as above but it includes the current move
        # nxbq -> nbd and it adds the time until the end, as we will stay in this cell and wont let others pieces in
        
        @cache
        def search( p, bq ) -> int:
            if p == len( pieces ):
                return 1

            res, t = 0, 0
            for m in moves[ pieces[p] ]:
                i, j = positions[p]
                # only start from initial position the first time.
                if t == 1:
                    i, j = i + m[0], j + m[1]
                nbq = bq
                    
                while i > 0 and i < 9 and j > 0 and j < 9:
                    if ( i, j, t ) in nbq:
                        break
                    nbq = nbq + (( i, j, t ),)
                    nxbq = nbq

                    # Figure out if we can stay in this cell until the end of the game
                    stay = True
                    for nt in range( t+1, 8 ):
                        if ( i, j, nt ) in bq:
                            stay = False
                        nxbq = nxbq + (( i, j, nt ),)

                    if stay:
                        res += search( p+1, nxbq )
                    i, j, t = i + m[0], j + m[1], t + 1
                
                i, j = positions[p]
                if ( i, j, 0 ) not in bq:
                    bq += (( i, j, 0 ),)
                t = 1
                    
            return res
        
        return search( 0, () )
            