/**
 * HTS Document Download Automation Script
 * Downloads PDF documents from three HTS sources for chapters 6-97
 */

const fs = require('fs');
const path = require('path');

// Base paths
const BASE_PATH = '/Users/ivi/VIBE/RATIOS/HTC/HTC-v1/HTS';

// Source configurations
const SOURCES = {
  WCO: {
    name: 'WCO',
    baseUrl: 'https://www.wcoomd.org/-/media/wco/public/global/pdf/topics/nomenclature/instruments-and-tools/hs-nomenclature-2022/2022/',
    getFilename: (chapter) => getWCOFilename(chapter),
    fileExtension: '_2022e.pdf'
  },
  CENSUS: {
    name: 'Census',
    baseUrl: 'https://www.census.gov/foreign-trade/schedules/b/2025/',
    getFilename: (chapter) => `c${chapter.toString().padStart(2, '0')}.pdf`,
    fileExtension: '.pdf'
  },
  USITC: {
    name: 'USITC',
    baseUrl: 'https://hts.usitc.gov/reststop/file?release=currentRelease&filename=',
    getFilename: (chapter) => `Chapter%20${chapter}`,
    fileExtension: '_2025HTSRev19.pdf'
  }
};

// WCO filename mapping (based on scraped patterns)
function getWCOFilename(chapter) {
  const chapterMappings = {
    1: '0101_2022e.pdf',
    2: '0102_2022e.pdf', 
    3: '0103_2022e.pdf',
    4: '0104_2022e.pdf',
    5: '0105_2022e.pdf',
    6: '0206_2022e.pdf',
    7: '0207_2022e.pdf',
    8: '0208_2022e.pdf',
    9: '0209_2022e.pdf',
    10: '0210_2022e.pdf',
    11: '0211_2022e.pdf',
    12: '0212_2022e.pdf',
    13: '0213_2022e.pdf',
    14: '0214_2022e.pdf',
    15: '0315_2022e.pdf',
    16: '0416_2022e.pdf',
    17: '0417_2022e.pdf',
    18: '0418_2022e.pdf',
    19: '0419_2022e.pdf',
    20: '0420_2022e.pdf',
    21: '0421_2022e.pdf',
    22: '0422_2022e.pdf',
    23: '0423_2022e.pdf',
    24: '0424_2022e.pdf',
    25: '0525_2022e.pdf',
    26: '0526_2022e.pdf',
    27: '0527_2022e.pdf',
    28: '0628_2022e.pdf',
    29: '0629_2022e.pdf',
    30: '0630_2022e.pdf',
    31: '0631_2022e.pdf',
    32: '0632_2022e.pdf',
    33: '0633_2022e.pdf',
    34: '0634_2022e.pdf',
    35: '0635_2022e.pdf',
    36: '0636_2022e.pdf',
    37: '0637_2022e.pdf',
    38: '0638_2022e.pdf',
    39: '0739_2022e.pdf',
    40: '0740_2022e.pdf',
    41: '0841_2022e.pdf',
    42: '0842_2022e.pdf',
    43: '0843_2022e.pdf',
    44: '0844_2022e.pdf',
    45: '0845_2022e.pdf',
    46: '0846_2022e.pdf',
    47: '0847_2022e.pdf',
    48: '0848_2022e.pdf',
    49: '0849_2022e.pdf',
    50: '1150_2022e.pdf',
    51: '1151_2022e.pdf',
    52: '1152_2022e.pdf',
    53: '1153_2022e.pdf',
    54: '1154_2022e.pdf',
    55: '1155_2022e.pdf',
    56: '1156_2022e.pdf',
    57: '1157_2022e.pdf',
    58: '1158_2022e.pdf',
    59: '1159_2022e.pdf',
    60: '1160_2022e.pdf',
    61: '1161_2022e.pdf',
    62: '1162_2022e.pdf',
    63: '1163_2022e.pdf',
    64: '1264_2022e.pdf',
    65: '1265_2022e.pdf',
    66: '1266_2022e.pdf',
    67: '1267_2022e.pdf',
    68: '1368_2022e.pdf',
    69: '1369_2022e.pdf',
    70: '1370_2022e.pdf',
    71: '1471_2022e.pdf',
    72: '1572_2022e.pdf',
    73: '1573_2022e.pdf',
    74: '1574_2022e.pdf',
    75: '1575_2022e.pdf',
    76: '1576_2022e.pdf',
    77: '1577_2022e.pdf',
    78: '1578_2022e.pdf',
    79: '1579_2022e.pdf',
    80: '1580_2022e.pdf',
    81: '1581_2022e.pdf',
    82: '1582_2022e.pdf',
    83: '1583_2022e.pdf',
    84: '1684_2022e.pdf',
    85: '1685_2022e.pdf',
    86: '1786_2022e.pdf',
    87: '1787_2022e.pdf',
    88: '1788_2022e.pdf',
    89: '1789_2022e.pdf',
    90: '1890_2022e.pdf',
    91: '1891_2022e.pdf',
    92: '1892_2022e.pdf',
    93: '1993_2022e.pdf',
    94: '2094_2022e.pdf',
    95: '2095_2022e.pdf',
    96: '2096_2022e.pdf',
    97: '2197_2022e.pdf'
  };
  
  return chapterMappings[chapter] || `${chapter.toString().padStart(4, '0')}_2022e.pdf`;
}

// Chapter folder mapping
function getChapterFolder(chapter) {
  const chapterNames = {
    6: 'Chapter_06_Live_Plants_Cut_Flowers',
    7: 'Chapter_07_Edible_Vegetables',
    8: 'Chapter_08_Edible_Fruit_Nuts',
    9: 'Chapter_09_Coffee_Tea_Spices',
    10: 'Chapter_10_Cereals',
    11: 'Chapter_11_Milling_Products_Starches',
    12: 'Chapter_12_Oil_Seeds_Industrial_Plants',
    13: 'Chapter_13_Lac_Gums_Plant_Extracts',
    14: 'Chapter_14_Vegetable_Plaiting_Materials',
    15: 'Chapter_15_Fats_Oils_Cleavage_Products',
    16: 'Chapter_16_Prepared_Meat_Fish',
    17: 'Chapter_17_Sugars_Confectionery',
    18: 'Chapter_18_Cocoa_Preparations',
    19: 'Chapter_19_Cereal_Preparations',
    20: 'Chapter_20_Prepared_Vegetables_Fruit',
    21: 'Chapter_21_Miscellaneous_Edible_Preparations',
    22: 'Chapter_22_Beverages_Spirits',
    23: 'Chapter_23_Food_Industry_Residues_Fodder',
    24: 'Chapter_24_Tobacco_Substitutes',
    25: 'Chapter_25_Salt_Sulphur_Stone',
    26: 'Chapter_26_Ores_Slag_Ash',
    27: 'Chapter_27_Mineral_Fuels_Oils',
    28: 'Chapter_28_Inorganic_Chemicals',
    29: 'Chapter_29_Organic_Chemicals',
    30: 'Chapter_30_Pharmaceutical_Products',
    31: 'Chapter_31_Fertilisers',
    32: 'Chapter_32_Tanning_Extracts_Dyes',
    33: 'Chapter_33_Essential_Oils_Cosmetics',
    34: 'Chapter_34_Soap_Cleaning_Preparations',
    35: 'Chapter_35_Proteins_Starches_Enzymes',
    36: 'Chapter_36_Explosives_Pyrotechnics',
    37: 'Chapter_37_Photographic_Goods',
    38: 'Chapter_38_Miscellaneous_Chemical_Products',
    39: 'Chapter_39_Plastics_Plastic_Articles',
    40: 'Chapter_40_Rubber_Rubber_Articles',
    41: 'Chapter_41_Raw_Hides_Leather',
    42: 'Chapter_42_Leather_Articles',
    43: 'Chapter_43_Furskins_Artificial_Fur',
    44: 'Chapter_44_Wood_Wood_Articles',
    45: 'Chapter_45_Cork_Cork_Articles',
    46: 'Chapter_46_Straw_Plaiting_Materials',
    47: 'Chapter_47_Pulp_Recovered_Paper',
    48: 'Chapter_48_Paper_Paperboard',
    49: 'Chapter_49_Printed_Books_Materials',
    50: 'Chapter_50_Silk',
    51: 'Chapter_51_Wool_Animal_Hair',
    52: 'Chapter_52_Cotton',
    53: 'Chapter_53_Other_Vegetable_Textile_Fibers',
    54: 'Chapter_54_Man_Made_Filaments',
    55: 'Chapter_55_Man_Made_Staple_Fibers',
    56: 'Chapter_56_Wadding_Felt_Nonwovens',
    57: 'Chapter_57_Carpets_Textile_Floor_Coverings',
    58: 'Chapter_58_Special_Woven_Fabrics',
    59: 'Chapter_59_Impregnated_Coated_Textile_Fabrics',
    60: 'Chapter_60_Knitted_Crocheted_Fabrics',
    61: 'Chapter_61_Knitted_Crocheted_Apparel',
    62: 'Chapter_62_Woven_Apparel_Clothing',
    63: 'Chapter_63_Other_Made_Up_Textile_Articles',
    64: 'Chapter_64_Footwear',
    65: 'Chapter_65_Headgear',
    66: 'Chapter_66_Umbrellas_Walking_Sticks',
    67: 'Chapter_67_Prepared_Feathers_Artificial_Flowers',
    68: 'Chapter_68_Stone_Articles',
    69: 'Chapter_69_Ceramic_Products',
    70: 'Chapter_70_Glass_Glassware',
    71: 'Chapter_71_Pearls_Precious_Stones_Metals',
    72: 'Chapter_72_Iron_Steel',
    73: 'Chapter_73_Iron_Steel_Articles',
    74: 'Chapter_74_Copper_Articles',
    75: 'Chapter_75_Nickel_Articles',
    76: 'Chapter_76_Aluminum_Articles',
    77: 'Chapter_77_Reserved',
    78: 'Chapter_78_Lead_Articles',
    79: 'Chapter_79_Zinc_Articles',
    80: 'Chapter_80_Tin_Articles',
    81: 'Chapter_81_Other_Base_Metals',
    82: 'Chapter_82_Tools_Cutlery',
    83: 'Chapter_83_Miscellaneous_Base_Metal_Articles',
    84: 'Chapter_84_Nuclear_Reactors_Machinery',
    85: 'Chapter_85_Electrical_Machinery',
    86: 'Chapter_86_Railway_Locomotives',
    87: 'Chapter_87_Motor_Vehicles',
    88: 'Chapter_88_Aircraft_Spacecraft',
    89: 'Chapter_89_Ships_Boats',
    90: 'Chapter_90_Optical_Measuring_Instruments',
    91: 'Chapter_91_Clocks_Watches',
    92: 'Chapter_92_Musical_Instruments',
    93: 'Chapter_93_Arms_Ammunition',
    94: 'Chapter_94_Furniture_Bedding',
    95: 'Chapter_95_Toys_Games_Sports_Equipment',
    96: 'Chapter_96_Miscellaneous_Manufactured_Articles',
    97: 'Chapter_97_Works_of_Art_Antiques'
  };
  
  return chapterNames[chapter] || `Chapter_${chapter.toString().padStart(2, '0')}`;
}

// Get section folder for a chapter
function getSectionFolder(chapter) {
  if (chapter >= 1 && chapter <= 5) return 'Section_I_Live_Animals_Animal_Products';
  if (chapter >= 6 && chapter <= 14) return 'Section_II_Vegetable_Products';
  if (chapter === 15) return 'Section_III_Fats_Oils_Cleavage_Products';
  if (chapter >= 16 && chapter <= 24) return 'Section_IV_Prepared_Foodstuffs_Beverages';
  if (chapter >= 25 && chapter <= 27) return 'Section_V_Mineral_Products';
  if (chapter >= 28 && chapter <= 38) return 'Section_VI_Chemical_Products';
  if (chapter >= 39 && chapter <= 40) return 'Section_VII_Plastics_Rubber';
  if (chapter >= 41 && chapter <= 43) return 'Section_VIII_Hides_Skins_Leather_Fur';
  if (chapter >= 44 && chapter <= 46) return 'Section_IX_Wood_Cork_Plaiting_Materials';
  if (chapter >= 47 && chapter <= 49) return 'Section_X_Pulp_Paper_Paperboard';
  if (chapter >= 50 && chapter <= 63) return 'Section_XI_Textiles_Textile_Articles';
  if (chapter >= 64 && chapter <= 67) return 'Section_XII_Footwear_Headgear_Accessories';
  if (chapter >= 68 && chapter <= 70) return 'Section_XIII_Stone_Ceramic_Glass';
  if (chapter === 71) return 'Section_XIV_Pearls_Precious_Stones_Metals';
  if (chapter >= 72 && chapter <= 83) return 'Section_XV_Base_Metals_Articles';
  if (chapter >= 84 && chapter <= 85) return 'Section_XVI_Machinery_Electrical_Equipment';
  if (chapter >= 86 && chapter <= 89) return 'Section_XVII_Transport_Equipment';
  if (chapter >= 90 && chapter <= 92) return 'Section_XVIII_Precision_Instruments_Apparatus';
  if (chapter === 93) return 'Section_XIX_Arms_Ammunition';
  if (chapter >= 94 && chapter <= 96) return 'Section_XX_Miscellaneous_Manufactured_Articles';
  if (chapter === 97) return 'Section_XXI_Works_of_Art_Antiques';
  
  return 'Unknown_Section';
}

// Main download function
async function downloadDocument(chapter, source, sourceName) {
  const url = source.baseUrl + source.getFilename(chapter);
  const sectionFolder = getSectionFolder(chapter);
  const chapterFolder = getChapterFolder(chapter);
  const targetDir = path.join(BASE_PATH, sectionFolder, chapterFolder);
  
  // Ensure target directory exists
  if (!fs.existsSync(targetDir)) {
    fs.mkdirSync(targetDir, { recursive: true });
  }
  
  let filename;
  if (sourceName === 'WCO') {
    filename = source.getFilename(chapter);
  } else if (sourceName === 'CENSUS') {
    filename = source.getFilename(chapter);
  } else if (sourceName === 'USITC') {
    filename = `Chapter ${chapter}_2025HTSRev19.pdf`;
  }
  
  const targetPath = path.join(targetDir, filename);
  
  console.log(`Downloading ${sourceName} Chapter ${chapter}: ${url}`);
  console.log(`Target: ${targetPath}`);
  
  return { url, targetPath, chapter, source: sourceName };
}

// Generate download tasks for chapters 6-97
function generateDownloadTasks() {
  const tasks = [];
  
  for (let chapter = 6; chapter <= 97; chapter++) {
    for (const [sourceName, source] of Object.entries(SOURCES)) {
      tasks.push(downloadDocument(chapter, source, sourceName));
    }
  }
  
  return tasks;
}

// Export for use with Puppeteer
module.exports = {
  SOURCES,
  generateDownloadTasks,
  getChapterFolder,
  getSectionFolder,
  BASE_PATH
};

// If run directly, show the tasks
if (require.main === module) {
  const tasks = generateDownloadTasks();
  console.log(`Generated ${tasks.length} download tasks for chapters 6-97`);
  console.log('Sample tasks:');
  tasks.slice(0, 6).forEach(task => {
    console.log(`- ${task.source} Ch${task.chapter}: ${task.url}`);
  });
}
