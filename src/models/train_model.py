import pandas as pd

from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Ridge
from sklearn.preprocessing import StandardScaler

import mlflow
import mlflow.sklearn

import logging
import sys


mlflow.set_tracking_uri( 'https://dagshub.com/yotitan/DA212O-PSET2.mlflow' )
tracking_uri = mlflow.get_tracking_uri( )
print( 'Current tracking uri: {}'.format(tracking_uri) )


logging.basicConfig( level=logging.WARN )
logger = logging.getLogger( __name__ )

def eval_metrics( actual, pred ):
    rmse = mean_squared_error( actual, pred, squared=False )
    mae = mean_absolute_error( actual, pred )
    r2 = r2_score( actual, pred )
    return rmse, mae, r2

def main( ):
    raw_df = pd.read_csv( '../../data/raw/boston_housing.csv' )
    
    train, test = train_test_split( raw_df )
    
    target = 'MEDV'
    features = raw_df.drop( columns=[target] ).columns
    
    train_x = train[features]
    test_x = test[features]
    train_y = train[target]
    test_y = test[target]

    std = StandardScaler( )
    train_x = std.fit_transform( train_x )
    test_x = std.transform( test_x )


    alpha = float( sys.argv[1] ) if len(sys.argv) > 1 else 0.5

    with mlflow.start_run( ):
        ridge_model = Ridge( alpha=alpha, random_state=42 )
        ridge_model.fit( train_x, train_y )

        test_pred = ridge_model.predict( test_x )

        ( rmse, mae, r2 ) = eval_metrics( test_y, test_pred )

        print( 'Ridge Regression model (alpha=%f):' % (alpha) )
        print( '\tRMSE : %s' % rmse )
        print( '\tMAE  : %s' % mae )
        print( '\tR2   : %s' % r2 )

        mlflow.log_param( 'alpha', alpha )
        mlflow.log_metric( 'rmse', rmse )
        mlflow.log_metric( 'r2', r2 )
        mlflow.log_metric( 'mae', mae )

        # tracking_url_type_store = urlparse(mlflow.get_tracking_uri()).scheme

        # Model registry 
        mlflow.sklearn.log_model( ridge_model, 'model' )

if __name__ == '__main__':
    main( )