## I will allow this class to have mongodb specific knowledge 
from pymongo.database import Database

class SeedSkus:
    
    def seedSkus(self, db: Database):
        if(db.migration.find_one({"name": "seedSkus1"}) == None):
            self.__seedSkus1(db)
            db.migration.insert_one({"name": "seedSkus1"})


    def __seedSkus1(self, db):
        db.products.insert_many(
            [{ "sku": "CM001", "product_type": "COFFEE_MACHINE_SMALL",	"water_line_compatible": False,  "model": "base"	 , "type": "COFFEE_MACHINE"  },
            { "sku": "CM002", "product_type": "COFFEE_MACHINE_SMALL",	"water_line_compatible": False,	"model": "premium"	 , "type": "COFFEE_MACHINE"  },
            { "sku": "CM003", "product_type": "COFFEE_MACHINE_SMALL",	"water_line_compatible": True,	"model" : "deluxe" , "type": "COFFEE_MACHINE"  },
            { "sku": "CM101", "product_type": "COFFEE_MACHINE_LARGE",	"water_line_compatible": False,	"model": "base" , "type": "COFFEE_MACHINE"  },
            { "sku": "CM102", "product_type": "COFFEE_MACHINE_LARGE",	"water_line_compatible": True,	"model": "premium" , "type": "COFFEE_MACHINE"  },
            { "sku": "CM103", "product_type": "COFFEE_MACHINE_LARGE",	"water_line_compatible": True,	"model" : "deluxe" , "type": "COFFEE_MACHINE"  },
            { "sku": "EM001", "product_type": "ESPRESSO_MACHINE",	"water_line_compatible": False,	"model": "base" , "type": "COFFEE_MACHINE"  },
            { "sku": "EM002", "product_type": "ESPRESSO_MACHINE",	"water_line_compatible": False,	"model": "premium" , "type": "COFFEE_MACHINE"  },
            { "sku": "EM003", "product_type": "ESPRESSO_MACHINE",	"water_line_compatible": True,	"model" : "deluxe" , "type": "COFFEE_MACHINE"  }]
        )
        db.products.insert_many(
            [{ "sku": "CP001", "product_type": "COFFEE_POD_SMALL",	"pack_size": "1 dozen", "coffee_flavor":	"COFFEE_FLAVOR_VANILLA" , "type": "COFFEE_POD"  },
            { "sku": "CP003", "product_type": "COFFEE_POD_SMALL",	"pack_size": "3 dozen",	"coffee_flavor":	"COFFEE_FLAVOR_VANILLA" , "type": "COFFEE_POD"  },
            { "sku": "CP011", "product_type": "COFFEE_POD_SMALL",	"pack_size": "1 dozen",	"coffee_flavor":	"COFFEE_FLAVOR_CARAMEL" , "type": "COFFEE_POD"  },
            { "sku": "CP013", "product_type": "COFFEE_POD_SMALL",	"pack_size": "3 dozen",	"coffee_flavor":	"COFFEE_FLAVOR_CARAMEL" , "type": "COFFEE_POD"  },
            { "sku": "CP021", "product_type": "COFFEE_POD_SMALL",	"pack_size": "1 dozen",	"coffee_flavor":	"COFFEE_FLAVOR_PSL" , "type": "COFFEE_POD"  },
            { "sku": "CP023", "product_type": "COFFEE_POD_SMALL",	"pack_size": "3 dozen",	"coffee_flavor":	"COFFEE_FLAVOR_PSL" , "type": "COFFEE_POD"  },
            { "sku": "CP031", "product_type": "COFFEE_POD_SMALL",	"pack_size": "1 dozen",	"coffee_flavor":	"COFFEE_FLAVOR_MOCHA" , "type": "COFFEE_POD"  },
            { "sku": "CP033", "product_type": "COFFEE_POD_SMALL",	"pack_size": "3 dozen",	"coffee_flavor":	"COFFEE_FLAVOR_MOCHA" , "type": "COFFEE_POD"  },
            { "sku": "CP041", "product_type": "COFFEE_POD_SMALL",	"pack_size": "1 dozen",	"coffee_flavor":	"COFFEE_FLAVOR_HAZELNUT" , "type": "COFFEE_POD"  },
            { "sku": "CP043", "product_type": "COFFEE_POD_SMALL",	"pack_size": "3 dozen",	"coffee_flavor":	"COFFEE_FLAVOR_HAZELNUT" , "type": "COFFEE_POD"  },
            { "sku": "CP101", "product_type": "COFFEE_POD_LARGE",	"pack_size": "1 dozen",	"coffee_flavor":	"COFFEE_FLAVOR_VANILLA" , "type": "COFFEE_POD"  },
            { "sku": "CP103", "product_type": "COFFEE_POD_LARGE",	"pack_size": "3 dozen",	"coffee_flavor":	"COFFEE_FLAVOR_VANILLA" , "type": "COFFEE_POD"  },
            { "sku": "CP111", "product_type": "COFFEE_POD_LARGE",	"pack_size": "1 dozen",	"coffee_flavor":	"COFFEE_FLAVOR_CARAMEL" , "type": "COFFEE_POD"  },
            { "sku": "CP113", "product_type": "COFFEE_POD_LARGE",	"pack_size": "3 dozen",	"coffee_flavor":	"COFFEE_FLAVOR_CARAMEL" , "type": "COFFEE_POD"  },
            { "sku": "CP121", "product_type": "COFFEE_POD_LARGE",	"pack_size": "1 dozen",	"coffee_flavor":	"COFFEE_FLAVOR_PSL" , "type": "COFFEE_POD"  },
            { "sku": "CP123", "product_type": "COFFEE_POD_LARGE",	"pack_size": "3 dozen",	"coffee_flavor":	"COFFEE_FLAVOR_PSL" , "type": "COFFEE_POD"  },
            { "sku": "CP131", "product_type": "COFFEE_POD_LARGE",	"pack_size": "1 dozen",	"coffee_flavor":	"COFFEE_FLAVOR_MOCHA" , "type": "COFFEE_POD"  },
            { "sku": "CP133", "product_type": "COFFEE_POD_LARGE",	"pack_size": "3 dozen",	"coffee_flavor":	"COFFEE_FLAVOR_MOCHA" , "type": "COFFEE_POD"  },
            { "sku": "CP141", "product_type": "COFFEE_POD_LARGE",	"pack_size": "1 dozen",	"coffee_flavor":	"COFFEE_FLAVOR_HAZELNUT" , "type": "COFFEE_POD"  },
            { "sku": "CP143", "product_type": "COFFEE_POD_LARGE",	"pack_size": "3 dozen",	"coffee_flavor":	"COFFEE_FLAVOR_HAZELNUT" , "type": "COFFEE_POD"  },
            { "sku": "EP003", "product_type": "ESPRESSO_POD",		"pack_size": "3 dozen",	"coffee_flavor":	"COFFEE_FLAVOR_VANILLA" , "type": "COFFEE_POD"  },
            { "sku": "EP005", "product_type": "ESPRESSO_POD",		"pack_size": "5 dozen",	"coffee_flavor":	"COFFEE_FLAVOR_VANILLA" , "type": "COFFEE_POD"  },
            { "sku": "EP007", "product_type": "ESPRESSO_POD",		"pack_size": "7 dozen",	"coffee_flavor":	"COFFEE_FLAVOR_VANILLA" , "type": "COFFEE_POD"  },
            { "sku": "EP013", "product_type": "ESPRESSO_POD",		"pack_size": "3 dozen",	"coffee_flavor":	"COFFEE_FLAVOR_CARAMEL" , "type": "COFFEE_POD"  },
            { "sku": "EP015", "product_type": "ESPRESSO_POD",		"pack_size": "5 dozen",	"coffee_flavor":	"COFFEE_FLAVOR_CARAMEL" , "type": "COFFEE_POD"  },
            { "sku": "EP017", "product_type": "ESPRESSO_POD",		"pack_size": "7 dozen",	"coffee_flavor":	"COFFEE_FLAVOR_CARAMEL" , "type": "COFFEE_POD"  }]
        )

        db.products.create_index( [("sku", 1)], unique=True )
        db.products.create_index( [("type", 1 )] )
        db.products.create_index( [("product_type", 1 )] )
        db.products.create_index( [("coffee_flavor", 1 )] )
        db.products.create_index( [("water_line_compatible", 1)] )
        db.products.create_index( [( "model", 1 )] )
        db.products.create_index( [( "pack_size", 1 )] )
        


