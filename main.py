from app import app
import os
import logging

app = app()

logging.basicConfig(level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

if(__name__) == '__main__':
    port = int(os.environ.get('PORT', 5000))
    logging.info(f'Iniciando o servidor na porta {port}')
    app.run(host="0.0.0.0", port=port, debug=False) #Mudança para debug=False em produção

